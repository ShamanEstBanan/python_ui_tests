from selenium.webdriver.common.by import By
from . import Locator


class TrySqlLocators(object):
    """
    Page https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
    """

    @property
    def title(self):
        return Locator("//head/title[contains(text(),'SQL Tryit Editor v1.6')]", By.XPATH)

    @property
    def input(self):
        return Locator("//*[@id='tryitform']", By.XPATH)

    @property
    def result_table(self):
        return Locator("//*[@id='divResultSQL']", By.XPATH)

    @property
    def result_strokes(self):
        return Locator('//*[@id="divResultSQL"]/div/table/tbody/tr', By.XPATH)

    @property
    def button_run(self):
        return Locator("//*[@type='button'][contains(text(),'Run SQL »')]", By.XPATH)

    def table_customers_contact_name(self, name: str):
        return Locator(
            f"//*[@id='divResultSQL']/div/table/tbody/tr/td[contains(text(),'{name}')]",
            By.XPATH,
        )

    def table_customers_address_by_contact_name(self, name: str):
        return Locator(
            f"//*[@id='divResultSQL']/div/table/tbody/tr/td[contains(text(),'{name}')]/following-sibling::td",
            By.XPATH,
        )
