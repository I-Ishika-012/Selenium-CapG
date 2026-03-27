"""

TS: valid username and invalid password
validate if its going to next page
if fails, capture ss
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep, strftime
import os

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
uname = driver.find_element(By.ID, "user-name")
passwd = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")
expected_url = "https://www.saucedemo.com/inventory.html"

uname.send_keys("standard_user")
passwd.send_keys("topsecretsauce")
login.click()
folder = os.path.join(os.getcwd(), "screenshots")
os.makedirs(folder, exist_ok=True)
ts = strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f"{folder}/err-{ts}.png")

assert driver.current_url == expected_url, "Invalid Login detected"

driver.close()



