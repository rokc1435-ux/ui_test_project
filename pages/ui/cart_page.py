from selenium.webdriver.common.by import By
from pages.ui.base_page import BasePage
class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    def checkout(self):
        self.click(self.CHECKOUT) 