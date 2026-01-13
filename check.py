from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\divya\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Path to your chromedriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)

sleep(5)
search = driver.find_element(By.NAME,"q")
search.send_keys("God")
search.clear()
search.send_keys("hello")
sleep(5)
v=driver.find_element(By.ID,"SIvCob").text()

print(v)
# driver.find_element(By.NAME,"btnK").click()
sleep(5)
# driver.quit()
input("Press Enter to exit...")

