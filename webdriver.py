from selenium import webdriver
import time 

class main_action:
    def __init__(self,driver):
        self.driver=driver
        self.get()
        self.driver.refresh()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.forward()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.minimize_window()
        time.sleep(3)
        self.driver.fullscreen_window()
        time.sleep(3)
        self.driver.set_window_size(128,800)
        time.sleep(3)
        self.driver.set_window_position(10,10)
        time.sleep(3)
        self.driver.close()
        time.sleep(3)
        self.driver.quit()

    def get(self):
        self.driver.get("https://artoftesting.com/samplesiteforselenium")
        time.sleep(3)
        # self.driver.quit()

driver1= webdriver.Chrome()
# driver1.implicitly_wait(10)
main_action(driver1)
# time.sleep(3)
# driver2=webdriver.Edge()
# main_action(driver2)
# time.sleep(3)
# driver3=webdriver.Firefox()
# main_action(driver3)
# time.sleep(3)

"""
if your using vscode as a beginner and the browser closes automatically:
1. using input("enter exit")
2. time.sleep(10)
3. using options---> from selenium.webdriver.chrome.options import Options
        opts=Option()
        opts.add_experrmental_option("detach", True)
        driver=webdriver.Chrome(options=opts)

"""

# input("enter exit")