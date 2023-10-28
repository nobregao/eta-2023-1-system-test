import pytest

class Test1:

    @pytest.mark.parametrize('all_browsers', ['chrome', 'firefox'])
    def test_click_login_button(self, run_all_browser):
        login_page = run_all_browser
        login_page.click_button_login()

        assert login_page.is_url(), 'Aplicação não permaneceu na mesma página!'
        assert login_page.message_field_error() == "Epic sadface: Username is required", 'Mensagem de erro inválida'
