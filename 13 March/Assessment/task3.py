"""
TASK 3
using id, partial selector
-go to amazon
-search mobiles -use id
-click on a product -use partial link text
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
mob=driver.find_element(By.LINK_TEXT, 'Mobiles')
mob.click()
sleep(2)
prod=driver.find_element(By.PARTIAL_LINK_TEXT, 'Poco C85 5G Power Black 8GB RAM 128GB ROM')
prod.click()