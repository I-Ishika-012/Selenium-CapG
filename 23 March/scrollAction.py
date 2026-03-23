from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
insta = driver.find_element(By.XPATH, "//a[.='Instagram']")
actions = ActionChains(driver)
# actions.move_to_element(insta).click(insta).perform()
# actions.scroll_to_element(insta)
# actions.pause(5)  # Gives the browser a moment to finish the scroll animation
# actions.move_to_element(insta) # Centers the mouse precisely
# actions.click()
# actions.perform()
# actions.scroll_by_amount(0,500).click().perform() --from wherever the mouse is located
# actions .scroll_from_origin(insta)
#move to element as mouse over
fresh = driver.find_element(By.XPATH, "//a[.='Fresh']")
actions.move_to_element(fresh).perform()
