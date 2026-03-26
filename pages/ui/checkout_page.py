from selenium.webdriver.common.by import By
from pages.ui.base_page import BasePage
class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    def get_complete_message(self):
        return self.find(self.COMPLETE_HEADER).text
   
    def fill_info(self, firstname, lastname, postalcode):
        self.input_text(self.FIRST_NAME, firstname)
        self.input_text(self.LAST_NAME, lastname)
        self.input_text(self.POSTAL_CODE,postalcode )
        self.click(self.CONTINUE_BTN)
    def confirm(self):
        self.click(self.FINISH_BTN)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
