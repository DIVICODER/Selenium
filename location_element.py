from selenium import webdriver
from selenium.webdriver.common import by  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time

#### you can also say from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.find_element(by.By.LINK_TEXT,"This is a link").click()
time.sleep(2)
driver.find_element(by.By.NAME,"firstName").send_keys("Hello")
time.sleep(2)
driver.find_element(by.By.ID,"idOfButton").click()
time.sleep(2)
driver.find_element(by.By.XPATH,"//button[text()='Generate Alert Box']").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)

# driver.find_element(by.By.ID,"male").click()  
gender="female"
if gender== "male":
    driver.find_element(by.By.ID,"male").click()
    time.sleep(2)

else:
    driver.find_element(by.By.ID,"female").click()
    time.sleep(2)





# radios=driver.find_elements(by.By.CSS_SELECTOR,"input[name='gender']")
# for r in radios:
#     r.click()
#     time.sleep(2)
#     assert r.is_selected()



'''we can use xpath, css_selector for radio button clicking'''

driver.find_element(by.By.CSS_SELECTOR,"input[type='checkbox']").click()
# x=driver.find_elements(by.By.CSS_SELECTOR,"form[action='#']")
# for y in x:
#     y.click()
# time.sleep(1)
time.sleep(1)

ddwn=driver.find_element(by.By.ID,"testingDropdown")
select=Select(ddwn)
select.select_by_index(1)
time.sleep(1)


# ActionChains(driver.find_element(by.By.ID, "dblClkBtn")).double_click()
ActionChains(driver).double_click(driver.find_element(by.By.ID, "dblClkBtn")).perform()
time.sleep(3)
driver.switch_to.alert.accept()


# driver.find_element(by.By.PARTIAL_LINK_TEXT,"Sample Script").click()
time.sleep(1)
driver.find_element(by.By.XPATH,"//button[text()='Generate Confirm Box']").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(2)

Image=driver.find_element(by.By.ID,"myImage")
Target=driver.find_element(by.By.ID,"targetDiv")
ActionChains(driver).drag_and_drop(Image,Target).perform()
driver.find_element(by.By.LINK_TEXT,"Selenium Sample Script").click()
driver.back()
time.sleep(3)