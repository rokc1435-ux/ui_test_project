from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ui.login_page import LoginPage

def test_login_success(driver):
    page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    page.login("standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

    

    
