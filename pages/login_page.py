from .base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):

    # locators = {
    #     "username_input": "#user-name",
    #     "password_input": "#password",
    #     "login_button": "#login-button"
    # }
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()