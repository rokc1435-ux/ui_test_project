
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.douban.com/")
wait = WebDriverWait(driver, 10)
login_iframe =wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//div[@class='login']/iframe")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"acconunt-tab-account.on"))).click()
username_input = driver.find_element(By.ID,"user-name")
username_input.send_keys("standard_user")
password_input = driver.find_element(By.NAME,"password")
password_input.send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
wait.until(EC.url_contains("inventory"))
print(driver.current_url)
driver.save_screenshot("login_success.png")
driver.quit()
