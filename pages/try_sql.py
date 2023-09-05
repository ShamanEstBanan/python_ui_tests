"""
Example of file with Page for test on main page of google.ru
"""
from pages import BasePage
from pages.locators.try_sql import TrySqlLocators
from settings import URL


class TrySql(BasePage):
    URL_PATH = '/sql/trysql.asp?filename=trysql_select_all'

    def __init__(self, browser):
        super(TrySql, self).__init__(browser)
        self.locators = TrySqlLocators()

    def open(self):
        self.open_page('%s%s' % (URL, self.URL_PATH))




