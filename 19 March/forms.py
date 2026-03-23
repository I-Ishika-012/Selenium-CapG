from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless") # For not opening the browser, still giving value to terminal using print statement
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys("Ram")
driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys("Krishn")
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("krishn@gmail.com")
driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys("741852963")
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
driver.find_element(By.XPATH, '//div[@aria-label="Choose Saturday, March 21st, 2026"]').click()
driver.find_element(By.XPATH, '//input[@value="Male"]').click()
driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("741852963 hehehehehe")
driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-1"]').click()
driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-3"]').click()
driver.find_element(By.XPATH, '//input[@id="uploadPicture"]').send_keys(r"D:\Extra work\CORE Subjects.docx")
driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys("helloooooooooooo")