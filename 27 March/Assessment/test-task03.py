from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

driver.implicitly_wait(10)

def test_scrollToFooter():
    footer = driver.find_element(By.XPATH, '//div[@class="footer-disclaimer"]')
    actions = ActionChains(driver)
    actions.scroll_to_element(footer).perform()
    sleep(2)
    fb = driver.find_element(By.XPATH, '//a[.="Facebook"]')
    fb.click()

def test_switchToFb():
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    mail = driver.find_element(By.XPATH, '//input[@name="email"]')
    mail.send_keys("clarkent@gmail.com")
    passwd = driver.find_element(By.XPATH, '//input[@name="pass"]')
    passwd.send_keys("not#superman")
    btn = driver.find_element(By.XPATH, '(//span[.="Log in"])[6]')
    btn.click()

sleep(5)
driver.quit()