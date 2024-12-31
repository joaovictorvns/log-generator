from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def select_log_level(self, level: str):
        log_level_element = self.driver.find_element(By.ID, value='logLevel')
        log_level = Select(log_level_element)
        log_level.select_by_value(level)

    def enter_log_message(self, message: str):
        log_message = self.driver.find_element(By.ID, value='logMessage')
        log_message.send_keys(message)

    def click_enable_log_extra_json_checkbox(self):
        checkbox = self.driver.find_element(By.ID, value='enableLogExtraJSON')
        checkbox.click()

    def enter_json_editor(self, json_text: str):
        json_editor = self.driver.find_element(By.CSS_SELECTOR, '.CodeMirror')
        json_editor.click()

        actions = ActionChains(self.driver)
        actions.send_keys(json_text)
        actions.perform()

    def clear_json_editor(self, is_mac: bool = False):
        json_editor = self.driver.find_element(By.CSS_SELECTOR, '.CodeMirror')
        json_editor.click()

        actions = ActionChains(self.driver)
        if is_mac:
            actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND)
        else:
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)
        actions.perform()

    def click_submit_button(self):
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            value='input[type=\'submit\']'
        )
        submit_button.click()

    def click_reset_button(self):
        reset_button = self.driver.find_element(
            By.CSS_SELECTOR,
            value='input[type=\'reset\']'
        )
        reset_button.click()

    def get_status(self) -> str:
        status = self.driver.find_element(By.ID, value='status')
        return status.text
