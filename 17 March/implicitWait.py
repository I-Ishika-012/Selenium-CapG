"""
IMPLICIT/GLOBAL WAIT
Implicit waits instruct the WebDriver to poll the DOM for a certain amount of time when trying to find
any element not immediately available. This is a global setting that applies to all find_element calls
for the entire session

polling freq-> 1/2 sec

--checks for presence of element
--if found returns the elem
--if not goes to implicit wait for req time
--checks for presence of element as per polling freq
--elem found within time, rest of wait time is preserved
--else returns elem not found, empty
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# sleep(2)
btn = driver.find_element(By.XPATH, "//button[text()='Start']")
btn.click()
driver.implicitly_wait(10)
hello = driver.find_element(By.XPATH, "//h4[text()='Hello World!']")
print(hello.text)
