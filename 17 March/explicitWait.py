from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//button").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
txt = driver.find_element(By.XPATH, "//div[@id='finish']/h4")

print(txt.text)

driver.quit()