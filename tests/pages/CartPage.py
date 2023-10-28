from selenium.webdriver.common.by import By

from tests.pages.Page import Page


class CartPage(Page):

    url = "https://www.saucedemo.com/cart.html"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def get_first_product_in_cart(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
