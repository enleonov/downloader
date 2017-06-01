"""Settings."""

import os
from datetime import datetime


PACKAGE_NAME = 'downloader'

LOG_LEVEL = os.getenv('DOWNLOADER_LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s\t%(levelname)s\tDOWNLOADER: %(message)s'

DATE_NULL_VALUE = datetime(year=3000, month=1, day=1)

THREADS_COUNT = 10

CHUNK_SIZE = 1024

BASE_PATH_DEFAULT = '/tmp/downloader'
TMP_PATH = BASE_PATH_DEFAULT + '/.tmp'

SFTP_PASSWORD_DEFAULT = ''
