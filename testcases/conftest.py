import pytest
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("opening chrome browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("launching edge")
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver
