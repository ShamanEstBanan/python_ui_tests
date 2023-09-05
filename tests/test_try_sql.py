import time

from pages.try_sql import TrySql


def test_customer_giovanni(browser):
    sql_page = TrySql(browser)
    sql_page.open()

    sql_page.click(sql_page.locators.button_run)

    assert sql_page.is_displayed(sql_page.locators.table_customers_contact_name('Maria Anders'))

    address = sql_page.find_element(sql_page.locators.table_customers_address_by_contact_name('Maria Anders'))
    expected_addres = 'Obere Str. 57'
    assert address.text == expected_addres, f"Expected address {expected_addres}, but actual {address.text}"
