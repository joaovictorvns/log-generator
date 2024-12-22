import http

from flask import Flask
from flask.testing import FlaskClient

from log_generator.controller.api_utils import ERROR_MESSAGES, SUCCESS_MESSAGE


def test_api_route_get(app: Flask, client: FlaskClient):
    response = client.get('/api')
    assert response.status_code == http.HTTPStatus.OK

    levels = ('debug', 'info', 'warning', 'error', 'critical')
    log_level_name = app.config['LOG_LEVEL'].lower()

    data = {
        'log_level_name': log_level_name,
        'log_level_number': levels.index(log_level_name) + 1,
    }

    assert response.json == data


def test_api_route_post_json_data_is_missing(client: FlaskClient):
    response = client.post('/api', json={})
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {'message': 'error', 'error': ERROR_MESSAGES[0]}

    assert response.json == expected_response_data


def test_api_route_post_level_field_is_required(client: FlaskClient):
    request_data = {'level': None}
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {'message': 'error', 'error': ERROR_MESSAGES[1]}

    assert response.json == expected_response_data


def test_api_route_post_level_field_must_be_a_str(client: FlaskClient):
    request_data = {'level': 0}
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {
        'message': 'error',
        'error': ERROR_MESSAGES[2],
    }

    assert response.json == expected_response_data


def test_api_route_post_invalid_log_level(client: FlaskClient):
    request_data = {'level': ''}
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {
        'message': 'error',
        'error': ERROR_MESSAGES[3].format(level=''),
    }

    assert response.json == expected_response_data


def test_api_route_post_message_field_is_required(
    app: Flask, client: FlaskClient
):
    request_data = {'level': app.config['LOG_LEVEL'].lower()}
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {
        'message': 'error',
        'error': ERROR_MESSAGES[4],
    }

    assert response.json == expected_response_data


def test_api_route_post_message_field_must_be_a_str(
    app: Flask, client: FlaskClient
):
    request_data = {'level': app.config['LOG_LEVEL'].lower(), 'message': 0}
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {
        'message': 'error',
        'error': ERROR_MESSAGES[5],
    }

    assert response.json == expected_response_data


def test_api_route_post_extra_field_must_be_a_dict(
    app: Flask, client: FlaskClient
):
    request_data = {
        'level': app.config['LOG_LEVEL'].lower(),
        'message': 'Testing...',
        'extra': 0,
    }
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST

    expected_response_data = {
        'message': 'error',
        'error': ERROR_MESSAGES[6],
    }

    assert response.json == expected_response_data


def test_api_route_post(app: Flask, client: FlaskClient):
    request_data = {
        'level': app.config['LOG_LEVEL'].lower(),
        'message': 'Testing...',
    }
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.OK

    expected_response_data = {'message': 'success', 'success': SUCCESS_MESSAGE}

    assert response.json == expected_response_data


def test_api_route_post_with_extra_field(app: Flask, client: FlaskClient):
    request_data = {
        'level': app.config['LOG_LEVEL'].lower(),
        'message': 'Testing...',
        'extra': {'text': 'Hello, World', 'number': 24},
    }
    response = client.post('/api', json=request_data)
    assert response.status_code == http.HTTPStatus.OK

    expected_response_data = {'message': 'success', 'success': SUCCESS_MESSAGE}

    assert response.json == expected_response_data
