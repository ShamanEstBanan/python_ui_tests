import time

from pages.try_sql import TrySql


class TestTrySQL(object):

    def test_customer_giovanni(self, browser):
        sql_page = TrySql(browser)
        sql_page.open()

        sql_page.click(sql_page.locators.button_run)
        assert sql_page.is_displayed(sql_page.locators.table_customers_contact_name('Giovanni Rovelli'))

        address = sql_page.find_element(
            sql_page.locators.table_customers_address_by_contact_name('Giovanni Rovelli'))

        expected_address = 'Via Ludovico il Moro 22'

        assert address.text == expected_address, f"Expected address {expected_address}, but actual {address.text}"

    def test_customer_from_london(self, browser):
        sql_page = TrySql(browser)

        sql_page.open()

        query = "SELECT * FROM Customers WHERE city = \"London\" ;"
        sql_page.input_sql_request(query)

        sql_page.click(sql_page.locators.button_run)

        result = sql_page.find_elements(sql_page.locators.result_strokes)
        result_count_lines = len(result[1:])

        expected_count_result_strokes = 6
        assert result_count_lines == expected_count_result_strokes, \
            f"Expected {expected_count_result_strokes} records where city = London, but given {result_count_lines} lines "

    def test_add_new_customer(self, browser):
        sql_page = TrySql(browser)

        sql_page.open()

        query = (
            'INSERT INTO Customers '
            'VALUES (777,"IOSIF KOBZON","Leonid Ukupnik", "Krasnaya ploshad", "Moscow", "00007", "RF")'
        )
        sql_page.input_sql_request(query)
        sql_page.click(sql_page.locators.button_run)
        sql_page.is_displayed(sql_page.locators.insert_result_success)

        query = "SELECT * FROM Customers WHERE CustomerID = \"777\" ;"
        sql_page.input_sql_request(query)

        sql_page.click(sql_page.locators.button_run)

        address = sql_page.find_element(
            sql_page.locators.table_customers_address_by_contact_name('Leonid Ukupnik'))

        expected_address = 'Krasnaya ploshad'

        assert address.text == expected_address, f"Expected address {expected_address}, but actual {address.text}"

    def test_update_customer(self, browser):
        sql_page = TrySql(browser)

        sql_page.open()

        query = ("UPDATE Customers "
                 "SET CustomerName=\"Serj\", ContactName=\"Tankian\", "
                 "Address=\"Tamanyan st\", City=\"Erevan\", PostalCode=\"0001\", Country=\"Armenia\""
                 "WHERE CustomerID=\"66\";")

        sql_page.input_sql_request(query)
        sql_page.click(sql_page.locators.button_run)
        sql_page.is_displayed(sql_page.locators.insert_result_success)

        query = "SELECT * FROM Customers WHERE CustomerID = \"66\" ;"
        sql_page.input_sql_request(query)
        sql_page.click(sql_page.locators.button_run)

        address = sql_page.find_element(
            sql_page.locators.table_customers_address_by_contact_name('Tankian'))

        expected_address = 'Tamanyan st'

        assert address.text == expected_address, f"Expected address {expected_address}, but actual {address.text}"

    def test_delete_customer(self, browser):
        sql_page = TrySql(browser)

        sql_page.open()

        sql_page.click(sql_page.locators.button_run)
