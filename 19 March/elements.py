from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.google.com")
driver.implicitly_wait(10)

# driver.find_element(By.TAG_NAME, "a").click()
links = driver.find_elements(By.TAG_NAME, "a")

print(links)
print(len(links))

for i in links:
    print(i.text, end=", ")