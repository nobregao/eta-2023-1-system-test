from selenium.webdriver.common.by import By

from tests.pages.Page import Page


class LoginPage(Page):

    url = "https://www.saucedemo.com/"

    def __init__(self):
        super(LoginPage, self).__init__(self.url)

    def click_button_login(self):
        button = self.driver.find_element(By.ID, "login-button")
        button.click()

    def message_field_error(self):
        element = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        return element.text

    def make_login(self, login_default="standard_user", password_default="secret_sauce"):
        self.driver.find_element(By.ID, "user-name").send_keys(login_default)
        self.driver.find_element(By.ID, "password").send_keys(password_default)

        self.driver.find_element(By.ID, "login-button").click()