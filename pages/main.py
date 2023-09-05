"""
Example of file with Page for test on main page of google.ru
"""
from pages import BasePage
from pages.locators.main import MainLocators
from settings import URL


class MainPage(BasePage):
    URL_PATH = '/'

    def __init__(self, browser):
        super(MainPage, self).__init__(browser)
        self.locators = MainLocators()

    def open(self):
        self.open_page('%s%s' % (URL, self.URL_PATH))

    def logo(self):
        return self.locators.logo