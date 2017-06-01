from urlparse import urlparse


class ParsedUrl(object):

    def __init__(self, url):
        self._parsed_url = urlparse(url)

    def get_hostname(self):
        return self._parsed_url.hostname

    def get_username(self):
        return self._parsed_url.username

    def get_password(self):
        return self._parsed_url.password

    def get_path(self):
        return self._parsed_url.path

    def get_protocol(self):
        return self._parsed_url.scheme

    def is_valid(self):
        return self._parsed_url.scheme and self._parsed_url.netloc
