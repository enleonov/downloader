import unittest

from configuration.config import Configuration


class DownloaderTestConfig(unittest.TestCase):

    def test_config_exist(self):
        self.assertIsNotNone(Configuration.get())

        base_path = Configuration.get_prop('data_path')
        self.assertIsNotNone(base_path)
