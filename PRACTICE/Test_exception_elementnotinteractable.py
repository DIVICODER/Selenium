from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")
driver.find_element(By.ID,"add_btn").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='confirmation']")))
enter_text=driver.find_element(By.XPATH,"//input[@type='text']").send_keys("text")
driver.find_element(By.NAME,"Save").click()
saved_text=driver.find_element(By.XPATH,"//input[@type='text']").text

assert saved_text=="text"