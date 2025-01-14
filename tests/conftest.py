import pytest
from dotenv import load_dotenv
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from log_generator import create_app
from tests.simple_live_server import SimpleLiveServer

load_dotenv()

BROWSER_CONFIG = {
    'chrome': {
        'service': ChromeService,
        'options': webdriver.ChromeOptions,
        'manager': ChromeDriverManager,
        'driver': webdriver.Chrome,
    },
    'firefox': {
        'service': FirefoxService,
        'options': webdriver.FirefoxOptions,
        'manager': GeckoDriverManager,
        'driver': webdriver.Firefox,
    },
    'edge': {
        'service': EdgeService,
        'options': webdriver.EdgeOptions,
        'manager': EdgeChromiumDriverManager,
        'driver': webdriver.Edge,
    }
}


@pytest.fixture(scope='session')
def app():
    return create_app()


@pytest.fixture(scope='module')
def simple_live_server(app: Flask):
    simple_live_server_ = SimpleLiveServer(app)
    simple_live_server_.start()
    yield simple_live_server_


def pytest_addoption(parser: pytest.Parser):
    app = create_app()

    parser.addoption(
        '--browsers',
        action='store',
        default=app.config['SELENIUM_BROWSERS'],
        help=('Comma-separated list of browsers to run tests on. Default is '
              '"chrome,firefox,edge" (can be set with FLASK_SELENIUM_BROWSERS '
              'env var).'),
    )

    parser.addoption(
        '--headless',
        action='store_true',
        default=app.config['SELENIUM_HEADLESS'],
        help=('Run tests in headless mode. Default is true (can be set with'
              ' FLASK_SELENIUM_HEADLESS env var).'),
    )


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'driver' in metafunc.fixturenames:
        browsers = metafunc.config.getoption('browsers').split(',')
        metafunc.parametrize('browser', browsers, scope='session')


@pytest.fixture(scope='session')
def driver(request: pytest.FixtureRequest, browser: str):
    browser_config = BROWSER_CONFIG.get(browser)
    headless = request.config.getoption('--headless')

    if not browser_config:
        raise ValueError(f'Unknown browser: {browser}')

    service = browser_config['service'](browser_config['manager']().install())
    options = browser_config['options']()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    driver_ = browser_config['driver'](service=service, options=options)

    try:
        yield driver_
    finally:
        driver_.quit()
