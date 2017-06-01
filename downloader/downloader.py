"""Main module of downloader."""

from threading import Thread
from Queue import Queue

from common.logger import logger
from common import settings
from common.utils.url import ParsedUrl
from common.utils import path
from protocols.protocol import Protocol


class Downloader(object):
    """Main class of downloader."""
    _query = None

    @classmethod
    def get_sources_list(cls):
        input_str = raw_input('For downloading enter urls, divided by comma: (eg <url_1>, <url_2>, ..)\n')
        str_list = input_str.split(',')
        sources_list = []
        for str_url in str_list:
            if len(str_url) > 0:
                sources_list.append(str_url.strip())
        logger.info('Sources list: %s' % sources_list)

        return sources_list if sources_list else None

    @classmethod
    def download_url(cls):
        while True:
            url = cls._query.get()

            data = Protocol.create(url)
            if data:
                if data.load():
                    data.save()

            cls._query.task_done()

    @classmethod
    def download(cls, sources_list):
        cls._query = Queue()
        for _ in range(settings.THREADS_COUNT):
            t = Thread(target=cls.download_url)
            t.daemon = True
            t.start()
        try:
            for url in sources_list:
                parsed_url = ParsedUrl(url)
                if parsed_url.is_valid():
                    cls._query.put(url)
                else:
                    logger.info('Invalid url: %s', url)
            cls._query.join()
        except KeyboardInterrupt:
            path.remove(settings.TMP_PATH)
            return
        path.remove(settings.TMP_PATH)

    @classmethod
    def run(cls):
        sources_list = cls.get_sources_list()
        if sources_list:
            logger.info('Start downloading. Sorces count: %s', len(sources_list))
            cls.download(sources_list)
            logger.info('Finish downloading')
        else:
            logger.info('Empty sources list')

"""
http://www.google.com, http://www.google.com, ftp://ftp.debian.org/debian/README.html


ftp://debian.org/debian-security/README.security

"""