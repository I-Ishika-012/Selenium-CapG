import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from time import sleep

@pytest.fixture
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("uname, passwd", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_login(driver, uname, passwd):

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(uname)
    driver.find_element(By.ID, "password").send_keys(passwd)
    driver.find_element(By.ID, "login-button").click()
    sleep(3)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"