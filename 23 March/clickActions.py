"""
single/double/context(right)
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.get("https://demoqa.com/buttons")
dbl = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(dbl).perform()

rightClick = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(rightClick).perform()

sngl = driver.find_element(By.XPATH, '//button[.="Click Me"]')
actions.click(sngl).perform()