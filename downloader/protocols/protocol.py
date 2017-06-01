"""Protocol classes for downloading sources."""
import paramiko

import urllib2

from common.logger import logger
from common.utils.url import ParsedUrl
from common.utils import path
from configuration.config import Configuration
from common import settings


def load_data_to_file(url, file_name):
    response = None
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        logger.info('HTTPError = %s, url: %s' + str(err.code), url)
        return False
    except urllib2.URLError, err:
        logger.info('URLError = %s, url: %s', str(err.reason), url)
        return False
    except Exception, err:
        logger.info('Error %s, url: %s', str(err.message), url)
        return False

    if response:
        with open(file_name, 'wb') as f:
            for chunk in iter(lambda: response.read(settings.CHUNK_SIZE), ''):
                f.write(chunk)

    return True


class Protocol(object):
    def __init__(self, url):
        self._url = url
        base_path = settings.TMP_PATH
        self._file_path = path.make_path(base_path, url)

    def create(url):
        parsed_url = ParsedUrl(url)
        protocol = parsed_url.get_protocol()
        if not protocol:
            logger.warn("Empty protocol for url: %s", url)
            return None
        if protocol == "http":
            return Http(url)
        if protocol == "ftp":
            return Ftp(url)
        if protocol == "sftp":
            return Sftp(url)

        logger.warn("Unknown protocol: %s", protocol)
        return None

    create = staticmethod(create)

    def save(self):
        base_path = Configuration.get_prop('data_path') or settings.BASE_PATH_DEFAULT
        path_from = self._file_path
        self._file_path = path.make_path(base_path, self._url)

        logger.debug('MOVE %s TO %s', path_from, self._file_path)
        path.move_data(path_from, self._file_path)


class Http(Protocol):
    def load(self):
        url = self._url
        file_name = self._file_path
        return load_data_to_file(url, file_name)


class Ftp(Protocol):
    def load(self):
        url = self._url
        file_name = self._file_path
        return load_data_to_file(url, file_name)


class Sftp(Protocol):
    def load(self):
        url = self._url
        file_name = self._file_path

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        parsed_url = ParsedUrl(url)
        password = parsed_url.get_password() or settings.SFTP_PASSWORD_DEFAULT

        ssh.connect(parsed_url.get_hostname(), username=parsed_url.get_username(), password=password)
        sftp = ssh.open_sftp()
        sftp.put(file_name, parsed_url.get_path())
        sftp.close()
        ssh.close()

        return True
