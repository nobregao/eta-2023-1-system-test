from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.Page import Page


class MenuPage(Page):

    btn_id_menu = "react-burger-menu-btn"
    btn_id_close = "react-burger-cross-btn"
    btn_logout = "logout_sidebar_link"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def open(self):
        self.driver.find_element(By.ID, self.btn_id_menu).click()

    def is_open(self):
        try:
            btn_close = WebDriverWait(self.driver, 4).until(
                expected_conditions.visibility_of_element_located((By.ID, self.btn_id_close))
            )
            return btn_close.is_displayed()
        except TimeoutException:
            return False

    def logout(self):
        self.driver.find_element(By.ID, self.btn_logout).click()
