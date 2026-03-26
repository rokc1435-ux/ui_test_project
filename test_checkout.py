import json
import pytest
from pages.ui.login_page import LoginPage
from pages.ui.cart_page import CartPage
from pages.ui.checkout_page import CheckoutPage 
from pages.ui.inventory_page import InventoryPage
with open("data/checkout_data.json") as f:
    data = json.load(f)
@pytest.mark.parametrize("checkout_data",data)
def test_checkout_flow(driver,checkout_data):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info(checkout_data["firstName"], checkout_data["lastName"], checkout_data["postalCode"])
    checkout_page.confirm()
    assert checkout_page.get_complete_message() == "Thank you for your order!"