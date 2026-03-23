from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.decathlon.in/")
driver.implicitly_wait(15)
prod = driver.find_element(By.XPATH, "//a[@href='https://www.decathlon.in/shop/Winter-Collection']")
prod.click()
product = driver.find_element(By.XPATH, "//a[@href='https://www.decathlon.in/c/beanies-headbands-82858']")
product.click()
