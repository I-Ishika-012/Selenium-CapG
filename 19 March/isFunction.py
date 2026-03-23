from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless") # For not opening the browser, still giving value to terminal using print statement
driver = Chrome(options=o)
driver.maximize_window()

'''driver.get("https://facebook.com")

ele = driver.find_element(By.XPATH, "//div[@aria-label='Log in']")
print(f"Displayed : {ele.is_displayed()}")
print(f"Enabled : {ele.is_enabled()}")

btn = driver.find_element(By.XPATH, "//input[@type='submit']")
print(f"Displayed : {btn.is_displayed()}")
print(f"Enabled : {btn.is_enabled()}")'''



'''driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
regBtn = driver.find_element(By.XPATH, "//button[@class='submitbtn resman-btn-primary resman-btn-regular resman-btn-disabled']")
print(f"Displayed : {regBtn.is_displayed()}")
print(f"Enabled : {regBtn.is_enabled()}")'''


driver.get("https://the-internet.herokuapp.com/checkboxes")

driver.implicitly_wait(10)

cBox1 = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
cBox1.click()
print(f"Selected : {cBox1.is_selected()}")

cBox2 = driver.find_element(By.XPATH, '//input[@type="checkbox"][2]')
cBox2.click()
print(f"Selected : {cBox2.is_selected()}")
# driver.quit()