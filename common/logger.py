"""Logger definition for all packages and modules."""

import logging

import settings


handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))
