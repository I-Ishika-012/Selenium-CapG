"""
XPATH - XML PATH
- traverse fwd ot bckwd
-locate elem based on text
-locate elem using attributes
-used for dynamic elem

TYPES:
-absolute
-relative

WAYS:
-using attributes
-using text
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
sleep(2)

name = driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]')
name.send_keys("Bruce Wayne")
sleep(2)

email = driver.find_element(By.XPATH, '//input[@type="email"]')
email.send_keys("Iamnotbatman@gmail.com")
sleep(2)

currAddress = driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]')
currAddress.send_keys("Wayne Manor, Gotham City")
sleep(2)

address = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
address.send_keys("Wayne Manor, Gotham City")
sleep(2)

submit = driver.find_element(By.XPATH, '//button[text()="Submit"]')
submit.click()
