import unittest

from common.utils.url import ParsedUrl


class DownloaderTestUrl(unittest.TestCase):

    def test_url(self):
        url = 'sftp://user:password@example.com:80/path0/file.txt'
        parsed_url = ParsedUrl(url)
        self.assertEqual(parsed_url.get_protocol(), 'sftp')
        self.assertEqual(parsed_url.get_hostname(), 'example.com')
        self.assertEqual(parsed_url.get_username(), 'user')
        self.assertEqual(parsed_url.get_password(), 'password')
        self.assertEqual(parsed_url.get_path(), '/path0/file.txt')
