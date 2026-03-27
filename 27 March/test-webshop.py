from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/")

class Test_WebShop:
    def test_register(self):
        reg = driver.find_element(By.XPATH, "//a[.='Register']")
        reg.click()
    def test_gender(self):
        gen = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
        gen.click()

    def test_fName(self):
        fname = driver.find_element(By.XPATH, '//input[@id="FirstName"]')
        fname.send_keys("Natasha")

    def test_lName(self):
        lname = driver.find_element(By.XPATH, '//input[@id="LastName"]')
        lname.send_keys("Romanov")

    def test_email(self):
        email = driver.find_element(By.XPATH, '//input[@id="Email"]')
        email.send_keys("romanov@gmail.com")

    def test_password(self):
        passwd = driver.find_element(By.XPATH, '//input[@id="Password"]')
        passwd.send_keys("nat@123")

    def test_confPasswd(self):
        confPasswd = driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]')
        confPasswd.send_keys("nat@123")

    def test_regBtn(self):
        btn = driver.find_element(By.XPATH, '//input[@id="register-button"]')
        btn.click()