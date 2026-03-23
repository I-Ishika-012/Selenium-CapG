'''implicit wait also called global wait, can be use in place of sleep
1. Helps managing and reducing time

“Hey Selenium, if you don’t find an element right away, wait for some time before giving up.”

# What it does?
Normally, Selenium tries to find an element immediately.
If it’s not there → it throws an error.

With implicit wait, Selenium will:

1. Keep checking for the element
2. Wait up to a specified time (like 10 seconds)
3. If the element appears → continue
4. If not → then show error
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)
driver.maximize_window()

# driver.implicitly_wait(10)
'''driver.get("https://decathlon.in/")
driver.find_element(By.XPATH, '//a[@href="https://www.decathlon.in/shop/Winter-Collection"]').click()
driver.find_element(By.XPATH, '//a[@href="https://www.decathlon.in/c/jackets-26192"]').click()'''



driver.get("https://the-internet.herokuapp.com/dynamic_loading")


driver.find_element(By.XPATH, "//a[contains(text(), 'hidden')]").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()

wait = WebDriverWait(driver, 10)
text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Hello')]")))
print(text.text)
# print(driver.find_element(By.XPATH, "//div[@id='finish']").text)