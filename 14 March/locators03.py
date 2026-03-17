'''
ALT WAYS TO USE CSS LOCATORS ID AND CLASS
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.amazon.in/")
sleep(2)
# search=driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox' )
# search = driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox' )
search = driver.find_element(By.CSS_SELECTOR, 'input[id="twotabsearchtextbox"]' )
search.send_keys("Cheese")
sleep(2)