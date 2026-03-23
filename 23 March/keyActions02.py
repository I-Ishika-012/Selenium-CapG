
"""
actionchains class

-create obj of class
-stores the actions
-use .perform() to implement

-click
-send keys
-drag/drop --mouse
-doubleclick --mouse

"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/text-box")

currAddress = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
currAddress.send_keys("Gotham City")
currAddress.send_keys(Keys.CONTROL + "a")
currAddress.send_keys(Keys.CONTROL + "c")

permAddress = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
permAddress.send_keys(Keys.CONTROL + "v")





