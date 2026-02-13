from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) #It calls the parent class constructor so that shared properties like the Playwright page instance are initialized in the BasePage. This allows all child page classes to access common methods and the page object.
        self.add_to_cart_button = page.locator("button[id^='add-to-cart']")
        self.cart_icon = page.locator("#shopping_cart_container")

    def add_to_cart_button(self):
        self.add_to_cart_button.first.click()

    def go_to_cart(self):
        self.cart_icon.click()