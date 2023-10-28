from tests.pages.CheckoutPage import CheckoutPage
from tests.pages.ProductPage import ProductPage
from tests.pages.CartPage import CartPage


class Test7:

    def test_valid_ordering_products_low_to_hight(self, login_saucedemo):

        product_page = ProductPage(login_saucedemo.driver)

        assert product_page.is_url(), 'Tela de home não foi aberta'

        product_page.order_products_by_low_to_high()

        all_prices = product_page.get_all_prices()
        all_prices_expected = sorted(all_prices.copy())

        assert all_prices_expected == all_prices, "Preços não estão ordenados"
