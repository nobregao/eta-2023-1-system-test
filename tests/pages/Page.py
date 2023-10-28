from selenium import webdriver


class Page:

    def __init__(self, url="", driver=None):
        self.url = url
        if driver is not None:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def is_url(self):
        return self.driver.current_url == self.url
