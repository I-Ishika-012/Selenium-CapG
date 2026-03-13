"""
TASK 1
using ID
-go to amazon
-click on update location
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt=ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.amazon.in/")
sleep(2)
location=driver.find_element(By.ID, "glow-ingress-line2")
location.click()