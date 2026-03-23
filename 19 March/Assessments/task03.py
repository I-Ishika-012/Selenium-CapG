from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://demowebshop.tricentis.com")

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//a[.="Register"]').click()

driver.find_element(By.XPATH, '//input[@id="gender-male"]').click()
driver.find_element(By.XPATH, '//input[@id="FirstName"]').send_keys("Ram")
driver.find_element(By.XPATH, '//input[@id="LastName"]').send_keys("krishn")
driver.find_element(By.XPATH, '//input[@id="Email"]').send_keys("ram@gmail.com")
driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys("ram@1234")
driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]').send_keys("ram@1234")
driver.find_element(By.XPATH, '//input[@id="register-button"]').click()

driver.quit()