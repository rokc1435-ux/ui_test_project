from selenium.webdriver.common.by import By
from pages.ui.base_page import BasePage

class InventoryPage(BasePage):
    ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.ID, "shopping_cart_container")

    def add_to_cart(self):
        self.click(self.ADD)

    def go_to_cart(self):
        self.click(self.CART)