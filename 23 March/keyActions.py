from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Perfume", Keys.ENTER)


