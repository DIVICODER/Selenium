from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")
driver.find_element(By.XPATH,"//button[@id='add_btn']").click()

# ############
# check=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='row2']")))
##############

check=driver.find_element(By.XPATH,"//div[@id='row2']")
assert check.is_displayed()