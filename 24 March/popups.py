"""

types of popups:

js alerts>>
-simple js alerts -- switch to alert mtd needs to be used here, using accept
-confirmation js alerts -- two options ok and cancel, select one
-prompt js alert -- req user input--provide i/p then click ok


"""

from time import sleep
from click import pause
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
#to disable notifications
opt.add_argument("--disable-notifications")
driver = Chrome(options=opt)

driver.maximize_window()

# driver.get("https://testautomationpractice.blogspot.com/")

#JS POPUPS
alertBtn = driver.find_element(By.XPATH, "//button[@id='alertBtn']")
alertBtn.click()
driver.switch_to.alert.accept()



