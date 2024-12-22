import pytest
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

from log_generator import create_app


@pytest.fixture(scope='module')
def app():
    return create_app()


# @pytest.fixture()
# def chrome_driver():
#     driver = webdriver.Chrome(
#         service=ChromeService(ChromeDriverManager().install())
#     )
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# @pytest.fixture()
# def firefox_driver():
#     driver = webdriver.Firefox(
#         service=FirefoxService(GeckoDriverManager().install())
#     )
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

# @pytest.fixture()
# def chrome_driver():
#     capabilities = DesiredCapabilities.CHROME
#     remote_url = 'http://localhost:4444/wd/hub'
#     driver = webdriver.Remote(
#         command_executor=remote_url,
#         desired_capabilities=capabilities
#     )
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
