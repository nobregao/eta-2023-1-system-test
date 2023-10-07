class Test1:

    def test_click_login_button(self, login_page):

        login_page.click_button_login()

        assert login_page.is_url(), 'Aplicação não permaneceu na mesma página!'
        assert login_page.message_field_error() == "Epic sadface: Username is required", 'Mensagem de erro inválida'
