"""
>>LOCATORS<<
--direct--
-ID
-NAME
-CLASS NAME
-TAG NAME

--text based--
-LINK TEXT
-PARTIAL LINK TEXT

--expression based--
-CSS SELECTORS
-XPATH
"""
from time import sleep

from selenium.webdriver.common.by import By

"""
>>ELEMENT ACTIONS<<
-send keys --user input/send text
-click --mouse actions
"""

from selenium.webdriver import Chrome, ChromeOptions
opt=ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(3)
# driver.find_element(By.ID, "userName").send_keys("John Doe")
#alt below
username = driver.find_element(By.ID, "userName")
username.send_keys("Jane Doe")
sleep(3)
submit = driver.find_element(By.ID, "submit")
submit.click()
sleep(3)
#USING TAG NAME
# passwd = driver.find_element(By.TAG_NAME, "INPUT")
# passwd.send_keys("verysecret")


