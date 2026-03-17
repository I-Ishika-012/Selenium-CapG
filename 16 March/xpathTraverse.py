"""
FWD AND BCKWD TRAVERSING USING XPATH
FWD -. parent to child -- use / or //
BCKWD -. child to parent -- use /..

METHODS TO LOCATE DYNAMIC ELEMENTS

MTD1--
step1 : identify static elements
step2 : from static elements, move back to common parent
step3 : from common parent, fetch dynamic elements

MTD2--
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_argument("--headless") #use --headless to not open browser everytime
driver = Chrome(options=opt)
driver.maximize_window()

# driver.get("https://demoqa.com/webtables")
# sleep(2)
# elem = driver.find_element(By.XPATH, '//td[text()="Cantrell"]/../td[5]') #fetching fifth child of the same row(parent)
# print(elem.text)
# sleep(2)
#
# driver.quit()

driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH, '//td[text()="Frank"]/../td[4]')
print(due.text)