from tests.pages.MenuPage import MenuPage


class Test3:

    def test_logout(self, login_saucedemo):

        menu_page = MenuPage(login_saucedemo.driver)
        menu_page.open()

        assert menu_page.is_open(), 'Menu is not open'

        menu_page.logout()

        assert login_saucedemo.is_url(), "URL de login não encontrado"
