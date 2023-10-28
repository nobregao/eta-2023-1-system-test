from tests.pages.CheckoutPage import CheckoutPage
from tests.pages.ProductPage import ProductPage
from tests.pages.CartPage import CartPage


class Test5:

    def test_valid_error_message_when_add_product(self, login_saucedemo):

        product_page = ProductPage(login_saucedemo.driver)
        product_name = product_page.add_random_product_to_cart()

        total_cart_items = 1
        assert product_page.get_cart_total_items() == total_cart_items, 'Produto não foi adicionado ao carrinho'
        product_page.open_cart_page()

        cart_page = CartPage(product_page.driver)
        assert cart_page.is_url(), 'Página do carrinho não foi aberta'

        product_in_cart = cart_page.get_first_product_in_cart()
        assert product_name == product_in_cart

        cart_page.click_checkout()

        checkout_page = CheckoutPage(product_page.driver)
        assert checkout_page.is_url(), 'URL inválida na página de checkout'

        checkout_page.click_continue()

        assert checkout_page.is_url(), 'Não permaneceu na página de checkout'

        assert checkout_page.get_message_error() == "Error: First Name is required"



