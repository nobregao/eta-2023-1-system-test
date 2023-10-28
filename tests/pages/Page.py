from selenium import webdriver


class Page:

    possible_browsers = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "safari": webdriver.Safari
    }

    # adding "--browser_selenium 'chrome'" in config for executing test case

    def __init__(self, url="", driver=None, browser=None):
        self.url = url
        self.driver = driver if driver is not None else self.possible_browsers[browser.strip().lower()]()

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def is_url(self):
        return self.driver.current_url == self.url
