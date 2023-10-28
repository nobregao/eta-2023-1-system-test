from tests.pages.ProductPage import ProductPage
from tests.pages.CartPage import CartPage


class Test4:

    def test_add_product_and_verify_cart_total_items(self, login_saucedemo):

        product_page = ProductPage(login_saucedemo.driver)
        product_name = product_page.add_random_product_to_cart()

        total_cart_items = 1
        assert product_page.get_cart_total_items() == total_cart_items, 'Produto não foi adicionado ao carrinho'
        product_page.open_cart_page()

        cart_page = CartPage(product_page.driver)
        assert cart_page.is_url(), 'Página do carrinho não foi aberta'

        product_in_cart = cart_page.get_first_product_in_cart()

        assert product_name == product_in_cart



