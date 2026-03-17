from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.amazon.in/")
sleep(2)

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Mobiles")
sleep(2)
btn = driver.find_element(By.ID, "nav-search-submit-button")
btn.click()
sleep(2)
price =driver.find_element(By.XPATH, "(//span[text()='₹'])[1]//following-sibling::span")
print(price.text)

sleep(3)
driver.close()