from selenium.webdriver.remote.webdriver import WebDriver


class SauceJobResult:
    def __init__(self, driver: WebDriver):
        self.__flag = False
        self.driver = driver

    def passed(self):
        self.__flag = True

    def failed(self):
        self.__flag = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        status = 'passed' if self.__flag else 'failed'
        self.driver.execute_script('sauce:job-result=' + status)
