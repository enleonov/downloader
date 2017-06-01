import unittest
import os

from common.utils import path


class DownloaderTestPath(unittest.TestCase):

    def test_path(self):
        base_path = '/tmp/test_downloader'
        url = 'http://example.com/path0/file.txt'
        file_path = '/tmp/test_downloader/http/example.com/path0/'
        path.make_path(base_path, url)
        self.assertTrue(os.path.exists(file_path))

        file_name = file_path + '/file.txt'
        with open(file_name, 'a'):
            os.utime(file_name, None)
        to_path = '/tmp/test_downloader/file.txt'
        path.move_data(file_name, to_path)
        self.assertTrue(os.path.exists(to_path))

        path.remove(base_path)
        self.assertFalse(os.path.exists(base_path))
