"""
TASK 4
-go to https://selenium.dev/
-click on downloads link text
-click on other pages exist
-fetch title
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt=ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://selenium.dev/")
sleep(2)
dwnld = driver.find_element(By.LINK_TEXT, "Downloads")
dwnld.click()
sleep(2)
lang = driver.find_element(By.PARTIAL_LINK_TEXT, "other languages exist")
lang.click()
sleep(2)

print(driver.title)
