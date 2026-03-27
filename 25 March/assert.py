"""
assert -- for validation
assert is used to determine whether expected o/p or behavior == actual outcome/behavior
-- if not gives assertion err --stops further exec

syntax
 expected = "Google Docs"
 actual = driver.title
assert expected condition == actual condition, "Err msg goes here"

"""

from time import sleep, strftime
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://www.google.com/")
assert driver.title == "Google", "Mismatch found"
search = driver.find_element(By.XPATH, "//textarea[@title='Search']")

search.send_keys("FBI")
sleep(2)
#SCREENSHOT ENTIRE PAGE
# driver.save_screenshot("search.png")
folder = os.path.join(os.getcwd(), "screenshots")
os.makedirs(folder, exist_ok=True)
# driver.save_screenshot(f"{folder}/screenshot.png")

#TIMESTAMP
ts = strftime("%Y%m%d-%H%M%S")
#SCREENSHOT OF AN ELEMENT
search.screenshot(f"{folder}/search-ele-{ts}.png")
driver.quit()
