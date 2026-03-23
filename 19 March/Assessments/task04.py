from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//input[@id="singleFileInput"]').send_keys(r"D:\Extra work\CORE Subjects.docx")

files = [r"D:\Extra work\CORE Subjects.docx", r"D:\Extra work\OOPS concepts.docx"]

for i in files:
    driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(i)