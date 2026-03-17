from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.flipkart.com/")
sleep(5)

search = driver.find_element(By.NAME, "q")
search.send_keys("Sneakers")
sleep(2)
btn = driver.find_element(By.XPATH, "//button[contains(@title,'Search')]")
btn.click()
sleep(2)
prod = driver.find_element(By.XPATH, "//a[contains(.,'DORIM Sneakers')]/following-sibling::a[1]//div[1]")
print(prod.text)


sleep(2)
driver.close()