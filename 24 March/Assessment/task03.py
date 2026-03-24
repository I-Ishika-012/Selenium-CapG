"""
-open 3 websites in separate tabs
-fetch title+url for all
-close all tabs except first
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://www.instagram.com/?hl=en")
print(f"Tab 1 ~ Title : {driver.title} , URL : {driver.current_url}")

driver.switch_to.new_window()

driver.get("https://google.com")
print(f"Tab 2 ~ Title : {driver.title} , URL : {driver.current_url}")

driver.switch_to.new_window()

driver.get("https://www.myntra.com/")
print(f"Tab 3 ~ Title : {driver.title} , URL : {driver.current_url}")

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()

sleep(5)
driver.quit()