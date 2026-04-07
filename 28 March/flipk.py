from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

# open flipkart
driver.get("https://www.flipkart.com/")
driver.maximize_window()

sleep(15)
# close login popup if appears
# try:
#     close_btn = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'X')]"))
#     )
#     close_btn.click()
# except:
#     pass

# hover on More dropdown
more = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'More')]"))
)
actions.move_to_element(more).perform()

# click 24x7 customer care
customer_care = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(.,'24x7 Customer Care')]"))
)
customer_care.click()