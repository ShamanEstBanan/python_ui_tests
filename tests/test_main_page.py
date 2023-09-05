from pages.main import MainPage


def test_logo_displayed(browser):
    main_page = MainPage(browser)
    main_page.open()
    assert main_page.is_displayed(main_page.logo())

