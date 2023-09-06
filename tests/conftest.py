import pytest
from selenium import webdriver

import settings


@pytest.fixture(scope="session")
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(settings.IMPLICITLY_WAIT)
    return chrome_browser
