"""Logging configuration for the application.

This module sets up logging for the application, using a custom `JSONFormatter`
to structure log messages in JSON format. The configuration is compatible with
observability tools and can be customized via environment variables.

Attributes:
    FLASK_LOG_PATH (str): The directory path where log files will be stored.
        Defaults to './log'.
    FLASK_LOG_LEVEL (str): The logging level. Defaults to 'DEBUG'.
    FLASK_PROJECT_NAME (str): The name of the project, used to name the log
        file. Defaults to 'app'.
    FLASK_PACKAGE_NAME (str): The package name of the project, used as the
        logger name. Defaults to 'app'.

Functions:
    setup_logging: Configures the logging system.
"""

import logging
import logging.config
import logging.handlers
import os
import pathlib

from log_generator.logging_formatter import JSONFormatter

LOG_PATH = os.getenv('FLASK_LOG_PATH', './log')
LOG_LEVEL = os.getenv('FLASK_LOG_LEVEL', 'DEBUG')
PROJECT_NAME = os.getenv('FLASK_PROJECT_NAME', 'app')
PACKAGE_NAME = os.getenv('FLASK_PACKAGE_NAME', 'app')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        PACKAGE_NAME: {
            'handlers': ['file'],
            'level': LOG_LEVEL,
            'propagate': True,
        }
    },
    'handlers': {
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/{PROJECT_NAME}.log',
            'encoding': 'utf-8',
            'formatter': 'json',
        }
    },
    'formatters': {
        'json': {
            '()': JSONFormatter,
        }
    },
}


def setup_logging():
    """Configures the logging system.

    Creates the log directory (if it doesn't exist) and applies the logging
    configuration defined in `LOGGING_CONFIG`.
    """
    pathlib.Path(LOG_PATH).mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)
