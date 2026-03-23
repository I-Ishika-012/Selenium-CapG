from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

sleep(2)
actions = ActionChains(driver)

#hover action
mHover = driver.find_element(By.XPATH, '//div[@class="dropdown"]')
actions.scroll_to_element(mHover).pause(2).move_to_element(mHover).perform()

sleep(2)

#click action
dblClick = driver.find_element(By.XPATH, '//button[.="Copy Text"]')
actions.double_click(dblClick).perform()

sleep(2)

#drag n drop
dragg = driver.find_element(By.XPATH, '//div[@id="draggable"]')
dropp = driver.find_element(By.XPATH, '//div[@id="droppable"]')
actions.drag_and_drop(dragg, dropp).perform()