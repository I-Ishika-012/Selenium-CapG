import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    yield driver
    driver.quit()