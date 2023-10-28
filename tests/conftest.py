import pytest

from tests.pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Ajuda aí jovem, passa o browser válido")

@pytest.fixture
def login_page(request):
    select_browser = request.config.getoption("--browser")
    login_page = LoginPage(browser=select_browser)
    login_page.open()

    yield login_page

    login_page.close()

@pytest.fixture
def login_saucedemo(login_page):
    login_page.make_login()
    yield login_page
