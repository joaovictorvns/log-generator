from selenium.webdriver.remote.webdriver import WebDriver

from log_generator.controller.api_utils import SUCCESS_MESSAGE
from tests.pages.home_page import HomePage
from tests.sauce_job_result import SauceJobResult
from tests.simple_live_server import SimpleLiveServer


def test_home_route_title_is_log_generator(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    home_page = HomePage(driver)
    home_page.open_page(simple_live_server.url())
    with SauceJobResult(driver) as sauce_job_result:
        assert home_page.get_title() == 'Log Generator'
        sauce_job_result.passed()


def test_home_route_record_logs_at_different_levels(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    levels = ('debug', 'info', 'warning', 'error', 'critical')

    home_page = HomePage(driver)
    home_page.open_page(simple_live_server.url())

    with SauceJobResult(driver) as sauce_job_result:
        for level in levels:
            home_page.select_log_level(level)
            home_page.enter_log_message(
                f'Test message at the {level} log level.'
            )
            home_page.click_submit_button()

            assert home_page.get_status() == f'Success: {SUCCESS_MESSAGE}'

            home_page.click_reset_button()
        sauce_job_result.passed()


def test_home_route_record_logs_at_different_levels_and_extra_fields(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    levels = ('debug', 'info', 'warning', 'error', 'critical')

    home_page = HomePage(driver)
    home_page.open_page(simple_live_server.url())

    with SauceJobResult(driver) as sauce_job_result:
        for level in levels:
            home_page.select_log_level(level)
            home_page.enter_log_message(
                f'Test message at the {level} log level.'
            )

            home_page.click_enable_log_extra_json_checkbox()
            home_page.clear_json_editor()
            home_page.enter_json_editor(f'{{"log_level_is": "{level}"}}')

            home_page.click_submit_button()

            assert home_page.get_status() == f'Success: {SUCCESS_MESSAGE}'

            home_page.click_reset_button()
        sauce_job_result.passed()


def test_home_route_submit_with_json_editor_in_different_error_cases(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    error_cases_and_expected = {
        '': 'Unexpected end of JSON input',
        '{""}': ('Expected \':\' after property name in JSON at position 3 '
                 '(line 1 column 4)'),
        '3.14': 'The "extra" field must be a dict',
    }

    home_page = HomePage(driver)
    home_page.open_page(simple_live_server.url())

    with SauceJobResult(driver) as sauce_job_result:
        for error_case in error_cases_and_expected:

            home_page.click_enable_log_extra_json_checkbox()
            home_page.clear_json_editor()
            home_page.enter_json_editor(error_case)

            home_page.click_submit_button()

            expected = error_cases_and_expected[error_case]
            assert home_page.get_status() == f'Error: {expected}'

            home_page.click_reset_button()
        sauce_job_result.passed()
