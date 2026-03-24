from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://www.zomato.com/india")
driver.implicitly_wait(100)

driver.find_element(By.XPATH, '//a[contains(text() , "Log")]').click()

driver.switch_to.frame( driver.find_element(By.XPATH, '//iframe[@id="auth-login-ui"]'))
sleep(2)
driver.find_element(By.XPATH, '//span[contains(text() , "Google")]').click()

sleep(5)
driver.quit()