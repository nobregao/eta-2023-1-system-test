from tests.pages.HomeProductPage import HomeProductPage


class Test2:

    def test_login_mostrar_produto(self, login_page):

        login_page.make_login()

        home_product_page = HomeProductPage(driver=login_page.driver)

        assert home_product_page.is_url(), 'Aplicação não mostrou página de produtos!'
        assert home_product_page.is_logged(), 'Usuário não logado'

        home_product_page.close()
