import pytest

from tests.pages.LoginPage import LoginPage


@pytest.fixture
def login_page():
    login_page = LoginPage()
    login_page.open()

    yield login_page

    login_page.close()

@pytest.fixture
def login_saucedemo(login_page):
    login_page.make_login()
    yield login_page
