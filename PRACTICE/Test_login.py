from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.switch_to.frame(0)
user_name=driver.find_element(By.ID,"username")
user_name.send_keys("student")
pass_word=driver.find_element(By.ID,"password")
pass_word.send_keys("Password123")
old_url=driver.current_url
but_ton=driver.find_element(By.ID,"submit").click()

WebDriverWait(driver,10).until(EC.url_changes(old_url))

new_url=driver.current_url
assert "logged-in-successfully" in new_url
# assert "Log Out" in new_url    ---------->> causes assertError as log out is not there in the new_url


# verify=driver.find_element(By.XPATH,"//h1[text()='Logged In Successfully']")
log_out=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Log out']")))
assert log_out.is_displayed()

log_out.click()


time.sleep(2)
driver.quit()



'''learnings-->
1. if your going to next page when you log in then use wait until the old url change using EC.url_changes()
2. if you need to check whether your moving to a corresponding https after logging in then you can check whether that /logged-in page is there
by checking its presence in the current url. 
3. if you need to check if something is there in the new page opened you can say them to wait and check if the visible element has this locater
present. and if so then you may perform action in that. 
4. to verify anything we use assert. as if it failes it shows asserterror.
5. most of the time we expected to get the 'element not found','time out','''