"""This module provides utility functions for the API."""

ERROR_MESSAGES = [
    'JSON data is missing.',
    'The "level" field is required.',
    'The "level" field must be a str.',
    (
        'Invalid log level: "{level}". '
        'Valid values are: "debug", "info", "warning", '
        '"error" and "critical"'
    ),
    'The "message" field is required.',
    'The "message" field must be a str.',
    'The "extra" field must be a dict.',
]

SUCCESS_MESSAGE = 'Log registered successfully'
