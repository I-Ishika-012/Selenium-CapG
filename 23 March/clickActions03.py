"""
DRAG AND DROP
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://demoqa.com/droppable")

drag = driver.find_element(By.XPATH, '//div[@id="draggable"]')
dropp = driver.find_element(By.XPATH, '//div[@id="droppable"]')

actions = ActionChains(driver)
actions.pause(2).drag_and_drop(drag, dropp).perform()