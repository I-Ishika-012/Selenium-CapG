"""
-open internetheroku
-go to js alerts
-perform all while fetching all alert texts
"""

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

btn = driver.find_element(By.XPATH, '//button[.="Click for JS Alert"]')
btn.click()
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.accept()
sleep(2)

confirm = driver.find_element(By.XPATH, '//button[.="Click for JS Confirm"]')
confirm.click()
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.accept()
sleep(2)

prompt = driver.find_element(By.XPATH, '//button[.="Click for JS Prompt"]')
prompt.click()
promptAlert = driver.switch_to.alert
print(promptAlert.text)
promptAlert.send_keys("I'm Batman")
sleep(2)
driver.switch_to.alert.accept()


sleep(5)
driver.quit()