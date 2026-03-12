"""
open wiki
refresh
fetch title
open amazon
fetch title
go back
close
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.get("https://www.wikipedia.org/")

driver.maximize_window()

sleep(4)

driver.refresh()

print(driver.title)

sleep(2)

driver.get("https://www.amazon.in/")

sleep(4)

print(driver.title)

driver.back()

sleep(2)

driver.quit()