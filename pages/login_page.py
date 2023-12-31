# pages/login_page.py
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    username_textbox = "//input[@id='user-name']"
    password_textbox = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    def enter_username(self, username):
        self.set_text(self.username_textbox, username)

    def enter_password(self, password):
        self.set_text(self.password_textbox, password)

    def click_login_button(self):
        self.click_element(self.login_button)
        time.sleep(10)
