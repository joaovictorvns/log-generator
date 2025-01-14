from selenium.webdriver.remote.webdriver import WebDriver

from log_generator.controller.api_utils import SUCCESS_MESSAGE
from tests.pages.ui_page import UIPage
from tests.simple_live_server import SimpleLiveServer


def test_ui_route_title_is_log_generator(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    ui_page = UIPage(driver)
    ui_page.open_page(simple_live_server.url())
    assert ui_page.get_title() == 'Log Generator'


def test_ui_route_record_logs_at_different_levels(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    levels = ('debug', 'info', 'warning', 'error', 'critical')

    ui_page = UIPage(driver)
    ui_page.open_page(simple_live_server.url())

    for level in levels:
        ui_page.select_log_level(level)
        ui_page.enter_log_message(
            f'Test message at the {level} log level.'
        )
        ui_page.click_submit_button()

        assert ui_page.get_status() == f'Success: {SUCCESS_MESSAGE}'

        ui_page.click_reset_button()


def test_ui_route_record_logs_at_different_levels_and_extra_fields(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    levels = ('debug', 'info', 'warning', 'error', 'critical')

    ui_page = UIPage(driver)
    ui_page.open_page(simple_live_server.url())

    for level in levels:
        ui_page.select_log_level(level)
        ui_page.enter_log_message(
            f'Test message at the {level} log level.'
        )

        ui_page.click_enable_log_extra_json_checkbox()
        ui_page.clear_json_editor()
        ui_page.enter_json_editor(f'{{"log_level_is": "{level}"}}')

        ui_page.click_submit_button()

        assert ui_page.get_status() == f'Success: {SUCCESS_MESSAGE}'

        ui_page.click_reset_button()


def test_ui_route_submit_with_json_editor_in_different_error_cases(
    driver: WebDriver, simple_live_server: SimpleLiveServer
):
    browser = driver.capabilities['browserName'].lower()
    print(browser)  # chrome or firefox
    error_cases_and_expected = {
        'chrome': {
            '': 'Unexpected end of JSON input',
            '{""}': ('Expected \':\' after property name in JSON at position 3'
                     ' (line 1 column 4)'),
            '3.14': 'The "extra" field must be a dict',
        },
        'firefox': {
            '': ('JSON.parse: unexpected end of data at line 1 column 1'
                 ' of the JSON data'),
            '{""}': ('JSON.parse: expected \':\' after property name in'
                     ' object at line 1 column 4 of the JSON data'),
            '3.14': 'The "extra" field must be a dict',
        },
        'microsoftedge': {
            '': ('Unexpected end of JSON input'),
            '{""}': ('Expected \':\' after property name in JSON at position 3'
                     ' (line 1 column 4)'),
            '3.14': 'The "extra" field must be a dict',
        }
    }

    ui_page = UIPage(driver)
    ui_page.open_page(simple_live_server.url())

    for error_case in error_cases_and_expected[browser]:
        ui_page.click_enable_log_extra_json_checkbox()
        ui_page.clear_json_editor()
        ui_page.enter_json_editor(error_case)

        ui_page.click_submit_button()

        expected = error_cases_and_expected[browser][error_case]
        assert ui_page.get_status() == f'Error: {expected}'

        ui_page.click_reset_button()
