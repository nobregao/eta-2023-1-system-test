from selenium.webdriver.common.by import By

from tests.pages.Page import Page


class CheckoutPage(Page):

    url = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_message_error(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message-container").text
