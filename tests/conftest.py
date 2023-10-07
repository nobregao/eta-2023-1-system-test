import pytest

from tests.pages.LoginPage import LoginPage


@pytest.fixture
def login_page():
    login_page = LoginPage()
    login_page.open()

    yield login_page

    login_page.close()
