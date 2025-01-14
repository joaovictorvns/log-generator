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
Functions:
    api_route: The route handler for the API endpoint.
    handle_get_request: Handles the GET request for retrieving log level info.
    handle_post_request: Handles the POST request for logging a message.
"""

import logging

from flask import Blueprint, current_app, jsonify, request

from log_generator.controller.api_utils import ERROR_MESSAGES, SUCCESS_MESSAGE

api_blueprint = Blueprint('api', __name__)
logger = logging.getLogger(__name__)


@api_blueprint.route('/api', methods=['GET', 'POST'])
def api_route():  # pylint: disable=inconsistent-return-statements
    """Handles the GET and POST requests for logging API.

    For GET requests:
        Returns the current log level name and its corresponding numeric value.

    For POST requests:
        Logs a message at the specified log level. The request should contain
        a JSON body with the fields "level", "message", and optionally "extra".
        It then returns a JSON response indicating success or error.
    """
    match request.method:
        case 'GET':
            response = handle_get_request()
        case 'POST':
            response = handle_post_request()

    if current_app.config.LOG_HEADERS:
        extra = {
            'client_ip': request.headers.get('X-Real-IP', request.remote_addr),
            'protocol': request.headers.get('X-Forwarded-Proto', 'http'),
            'http_method': request.method,
            'request_url': request.url,
            'user_agent': request.headers.get('User-Agent'),
            'referer': request.headers.get('Referer'),
            'host': request.headers.get('Host'),
            'status_code': response[1],
            'request_data': request.json if request.is_json else None,
        }
        logger.info('Proxy Headers', extra=extra)
    return response


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

    return jsonify(data), 200


def handle_post_request():
    """Handles POST request for logging a message.

    This function processes the JSON body of the request to log a message with
    the specified log level. The request must include the fields "level",
    "message", and optionally "extra". If validation fails, an error message
    is returned. It then returns a JSON response indicating success or error.
    """
    try:
        if not request.json:
            raise ValueError(ERROR_MESSAGES[0])

        level = request.json.get('level')
        message = request.json.get('message')
        extra = request.json.get('extra')

        if level is None:
            raise ValueError(ERROR_MESSAGES[1])

        if not isinstance(level, str):
            raise ValueError(ERROR_MESSAGES[2])

        if level not in {'debug', 'info', 'warning', 'error', 'critical'}:
            raise ValueError(ERROR_MESSAGES[3].format(level=level))

        if message is None:
            raise ValueError(ERROR_MESSAGES[4])

        if not isinstance(message, str):
            raise ValueError(ERROR_MESSAGES[5])

        if extra is not None and not isinstance(extra, dict):
            raise ValueError(ERROR_MESSAGES[6])

        getattr(logger, level)(msg=message, extra=extra)

        data = {'message': 'success', 'success': SUCCESS_MESSAGE}
        return jsonify(data), 200
    except (ValueError, KeyError) as err:
        logger.exception('Failed to log message')
        data = {'message': 'error', 'error': str(err)}
        return jsonify(data), 400
