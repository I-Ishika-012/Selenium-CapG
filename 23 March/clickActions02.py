"""
click and hold/release
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
actions = ActionChains(driver)
sleep(2)
cross = driver.find_element(By.XPATH, '//span[@class="ng-tns-c2785778308-3 icon-cancel"]').click()
sleep(2)
passwd = driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("topsecret")
viewpasswd = driver.find_element(By.XPATH, '//button[@tabindex="0"]')
actions.pause(2).click_and_hold(viewpasswd).pause(2).release().perform()