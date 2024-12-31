import datetime
import os

import pytest
from dotenv import load_dotenv
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from log_generator import create_app
from tests.simple_live_server import SimpleLiveServer

load_dotenv()


@pytest.fixture(scope='session')
def app():
    return create_app()


@pytest.fixture(scope='module')
def simple_live_server(app: Flask):
    simple_live_server_ = SimpleLiveServer(app)
    simple_live_server_.start()
    yield simple_live_server_


@pytest.fixture(scope='session')
def driver():
    project_name = os.getenv('FLASK_PROJECT_NAME')

    username = os.getenv('SAUCE_USERNAME')
    access_key = os.getenv('SAUCE_ACCESS_KEY')
    tunnel_name = os.getenv('SAUCE_TUNNEL_NAME')

    browser = os.getenv('SELENIUM_BROWSER')
    browser_version = os.getenv('SELENIUM_BROWSER_VERSION')
    platform_name = os.getenv('SELENIUM_PLATFORM_NAME')

    options = None
    match browser:
        case 'chrome':
            options = ChromeOptions()
        case 'firefox':
            options = FirefoxOptions()

    options.browser_version = browser_version
    options.platform_name = platform_name

    datetime_now = datetime.datetime.now()
    build = f'{project_name}-{datetime_now.strftime("%Y-%m-%d")}'
    aux = platform_name.lower().replace(' ', '-')
    name = f'{project_name}-{aux}-{browser}-{browser_version}'

    sauce_options = {
        'username': username,
        'accessKey': access_key,
        'build': build,
        'name': name,
        'tunnelName': tunnel_name,
    }

    options.set_capability('sauce:options', sauce_options)

    url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'

    driver_ = webdriver.Remote(command_executor=url, options=options)
    driver_.implicitly_wait(10)

    yield driver_

    driver_.quit()
