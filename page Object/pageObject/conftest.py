import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language, exp. '--language=es'")
    parser.addoption('--browser', action='store', default=None,
                     help="Choose browser, exp. '--browser=chrome'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()
    else:
        raise pytest.UsageError("--browser should be chrome")

    