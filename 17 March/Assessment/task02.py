from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://demoqa.com/webtables")

wait = WebDriverWait(driver, 100)

name = wait.until(EC.visibility_of_element_located((By.XPATH, '(//tr)[5]//td[1]'))).text
salary = wait.until(EC.visibility_of_element_located((By.XPATH, '(//tr)[5]//td[1]/../td[5]'))).text
print(f"{name}'s salary is {salary}")
#OR

# print(wait.until(EC.visibility_of_element_located((By.XPATH, '//td[.="Kierra"]/../td[5]'))).text)

# OR

# print(wait.until(EC.visibility_of_element_located((By.XPATH, '//td[text()="Kierra"]//following-sibling::td[4]'))).text)

driver.quit()