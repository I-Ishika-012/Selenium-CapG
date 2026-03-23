from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://flipkart.com")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="b3wTlE"]'))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='nw1UBF v1zwn25']"))).send_keys("Mobile")
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
print(wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="lvJbLV col-12-12"][6]//div)[15]'))).text)

driver.quit()