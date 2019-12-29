from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "There is no 'login' in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "There is no register form"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()
