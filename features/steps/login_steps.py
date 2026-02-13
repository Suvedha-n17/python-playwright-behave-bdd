from behave import given, when, then

from pages.inventoy_page import InventoryPage
from pages.login_page import LoginPage


@given("the user is on the SauceDemo login page")
def step_impl(context):
    registration_url = f"{context.base_url}"
    if not hasattr(context, "page") or context.page is None:
        raise RuntimeError("context.page is not initialized")
    context.login_page = LoginPage(context.page)
    context.login_page.goto(registration_url)
    context.login_page.take_screenshot("login_page")

@when("they enter valid credentials")
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")
    context.login_page.take_screenshot("after_login")

@then("they should be redirected to the inventory page")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url
    context.inventory_page.take_screenshot("inventory_page")


