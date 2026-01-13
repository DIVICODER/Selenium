from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("incorrectPassword")

driver.find_element(By.ID,"submit").click()

verify_error_msg=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"error")))
assert verify_error_msg.is_displayed()
time.sleep(1)

assert verify_error_msg.text == "Your password is invalid!"