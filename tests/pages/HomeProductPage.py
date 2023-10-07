from selenium.webdriver.common.by import By

from tests.pages.Page import Page


class HomeProductPage(Page):

    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super(HomeProductPage, self).__init__(self.url, driver=driver)

    def is_logged(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
