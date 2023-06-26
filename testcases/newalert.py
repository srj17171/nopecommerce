import math
import time

from selenium.webdriver import ActionChains


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")
# time.sleep(3)
# action = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
# action.double_click(element).perform()
# time.sleep(3)
# Alert(driver).accept()
# time.sleep(3)
# driver.get("https://omayo.blogspot.com/")
# time.sleep(4)
# alert = driver.find_element(By.XPATH, "//input[@id='alert1']").click()
# time.sleep(4)
# alert = driver.switch_to.alert
# alert.accept()
# # for dismiss alert.dismiss()
# time.sleep(4)


#----2nd way-----------
# ----- by using Alert class (from selenium.webdriver.common.alert import Alert)
# Alert(driver).accept()

# driver.get("https://the-internet.herokuapp.com/windows")
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
# time.sleep(5)
# windowes = driver.window_handles
# print(windowes)
# print(driver.current_window_handle)
# driver.switch_to.window(windowes[0])
# time.sleep(2)

class Area1:

    def area(self, r):
        return math.pi*r*r

class Area2(Area1):

    def area(self, a, b):
        return a * b

# ab = Area2()
# print(ab.area(5, 2))

class New:

    def area(self, a, b, c=1):
        return a * b * c

a = New()
a.area(2, 3, 4)