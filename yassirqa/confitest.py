import pytest
from selenium import webdriver

supported_browsers = ['chrome', 'firefox']


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not supported. Supported are: {supported_browsers}")
    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox',):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()
