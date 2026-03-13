'''
USING NAME
-OPEN FB
-ENTER EMAIL PASS
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.facebook.com/home.php")
sleep(2)
email = driver.find_element(By.NAME,"email")
email.send_keys("Bruce Wayne")
sleep(2)
password = driver.find_element(By.NAME, "pass")
password.send_keys("iamnot@batman")