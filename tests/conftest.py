import pytest
import settings
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    chrome_browser = webdriver.Chrome(options=options)

    chrome_browser.implicitly_wait(settings.IMPLICITLY_WAIT)
    return chrome_browser
