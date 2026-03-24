"""
open twitter
click on signup with google
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://x.com/?lang=en")
wait = WebDriverWait(driver, 10)

# wait & switch to iframe
iframe = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//iframe[@title='Sign in with Google Button']")
))
driver.switch_to.frame(iframe)

# now locate the actual button inside iframe
google_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='button']")   # may vary
))
google_btn.click()