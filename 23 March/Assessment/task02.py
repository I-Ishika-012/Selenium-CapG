from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("https://www.nike.in/")
driver.implicitly_wait(10)

actions = ActionChains(driver)

kids = driver.find_element(By.XPATH, '//div[@class="css-b0dwlh"][4]')
actions.move_to_element(kids).pause(2).click(kids).perform()

driver.switch_to.window(driver.window_handles[1])

shop = driver.find_element(By.XPATH, '//a[@aria-label="Shop"]')
actions.scroll_to_element(shop).pause(2).click(shop).perform()

shoes = driver.find_element(By.XPATH, '(//div[@class="css-1sjxv95"])[14]')
actions.scroll_to_element(shoes).pause(2).click(shoes).perform()

driver.switch_to.window(driver.window_handles[2])

shoesSize = driver.find_element(By.XPATH, '//label[.="UK 4"]')
actions.click(shoesSize).perform()

addToBag = driver.find_element(By.XPATH, '//button[@class="addToBagButtonContainer  css-1448vw4"]')
actions.click(addToBag).perform()