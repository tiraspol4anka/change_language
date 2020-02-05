import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="chrome")

    parser.addoption('--language', action='store', default=None, help="en, ru, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser_name == "chrome"
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()