from selenium.webdriver.common.by import By
from . import Locator


class MainLocators(object):
    """
    Main page w3schools.com
    """

    @property
    def logo(self):
        return Locator('//*[@id="pagetop"]/a[1]/i', By.XPATH)
