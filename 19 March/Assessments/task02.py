from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

ele1 = driver.find_elements(By.XPATH, "//div[@id='nav-main']//a")

print(len(ele1))
for i in range(len(ele1)):
    print(f"{(ele1[i]).text} -> {ele1[i].get_attribute('href')}")
