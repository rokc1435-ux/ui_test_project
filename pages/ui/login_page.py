from selenium.webdriver.common.by import By
from pages.ui.base_page import BasePage


class LoginPage(BasePage):
    # 定位器放这里
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//input[@id='login-button']")
    def login(self, username, password):
        self.input_text(self.USERNAME,username)
        self.input_text(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)