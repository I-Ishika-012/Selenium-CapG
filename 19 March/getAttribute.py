from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.google.com")

driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH, "//a[@class='gb_A']")
print(ele.get_attribute("aria-label"))
