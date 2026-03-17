"""
XPATH
-Using contains attributes/text
-//tagname[contains(@attribute, 'value')]
-//tagname[contains(text(), 'webtext')]
-//tagname[contains( . , 'webtext')]
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.amazon.in/")
sleep(3)
prod = driver.find_element(By.XPATH, "//span[text()='Refrigerators']")
prod.click()
sleep(3)
# lnk = driver.find_element(By.XPATH, '//a[contains(., "Amazon Accelerator")]')
lnk = driver.find_element(By.XPATH, '//a[contains(@href, "accelerator")]')
lnk.click()