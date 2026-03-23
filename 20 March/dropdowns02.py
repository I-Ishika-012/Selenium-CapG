from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.amazon.in")
sleep(2)
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Puma")
sleep(2)
wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "s-suggestion"))
)
suggestions = driver.find_elements(By.CLASS_NAME, "s-suggestion")
for s in suggestions:
    print(s.text)
sleep(2)
driver.quit()