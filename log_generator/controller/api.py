"""API Blueprint for logging messages.

This module defines a Flask Blueprint (`api_blueprint`) that handles the
endpoint (`/api`).

Two HTTP methods are defined for this endpoint:
- `GET`: Returns the current log level and its numeric value.
- `POST`: Accepts a JSON payload to log a message with the specified log level.

It also handles validation of the input data for the `POST` method, including
required fields and data types.

Attributes:
    api_blueprint (flask.Blueprint): The Flask Blueprint for the API routes.
    logger (logging.Logger): The logger instance used to log messages.
"""

import logging

from flask import Blueprint, current_app, jsonify, request

api_blueprint = Blueprint('api', __name__)
logger = logging.getLogger(__name__)


@api_blueprint.route('/api', methods=['GET', 'POST'])
def api_route():
    """Handles the GET and POST requests for logging API.

    For GET requests:
        Returns the current log level name and its corresponding numeric value.

    For POST requests:
        Logs a message at the specified log level. The request should contain
        a JSON body with the fields "level", "message", and optionally "extra".
        It then returns a JSON response indicating success or error.
    """
    if request.method == 'GET':
        return handle_get_request()

    if request.method == 'POST':
        return handle_post_request()
    return None


def handle_get_request():
    """Handles GET request for retrieving log level information.

    This function gets the log level name and number from the Flask application
    configuration and returns them in a JSON response.
    """
    levels = ('debug', 'info', 'warning', 'error', 'critical')
    log_level_name = current_app.config.LOG_LEVEL.lower()

    data = {
        'log_level_name': log_level_name,
        'log_level_number': levels.index(log_level_name) + 1,
    }

    return jsonify(data)


def handle_post_request():
    """Handles POST request for logging a message.

    This function processes the JSON body of the request to log a message with
    the specified log level. The request must include the fields "level",
    "message", and optionally "extra". If validation fails, an error message
    is returned. It then returns a JSON response indicating success or error.
    """
    try:
        if not request.json:
            raise ValueError('JSON data is missing.')

        level = request.json.get('level')
        message = request.json.get('message')
        extra = request.json.get('extra')

        if level is None:
            raise ValueError('The "level" field is required')

        if not isinstance(level, str):
            raise ValueError('The "level" field must be a str.')

        if level not in {'debug', 'info', 'warning', 'error', 'critical'}:
            raise ValueError(
                f'Invalid log level: "{level}". '
                'Valid values are: "debug", "info", "warning", '
                '"error" and "critical"'
            )

        if message is None:
            raise ValueError('The "message" field is required')

        if not isinstance(message, str):
            raise ValueError('The "message" field must be a str.')

        if extra is not None and not isinstance(extra, dict):
            raise ValueError('The "extra" field must be a dict.')

        getattr(logger, level)(msg=message, extra=extra)

        data = {'message': 'success', 'success': 'Log registered successfully'}
        return jsonify(data), 200
    except (ValueError, KeyError) as err:
        logger.exception('Failed to log message.')
        data = {'message': 'error', 'error': str(err)}
        return jsonify(data), 400
