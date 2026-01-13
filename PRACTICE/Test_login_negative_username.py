from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("incorrectUser")
time.sleep(1)
driver.find_element(By.ID,"password").send_keys("Password123")
time.sleep(1)
driver.find_element(By.ID,"submit").click()
time.sleep(1)
# error=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(driver.find_element(By.ID,"error")))
error=WebDriverWait(driver,10).until(EC.visibility_of_element_located(((By.ID,"error"))))
time.sleep(1)
assert error.is_displayed() 
assert error.text =="Your username is invalid!"

