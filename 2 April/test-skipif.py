from time import sleep

import pytest
from selenium import webdriver

#this will always be skipped
@pytest.mark.skip(reason="Feature not ready yet")
def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()


browser = "chrome"

#condition based skip
@pytest.mark.skipif(browser != "chrome", reason="Test only for Chrome")
def test_only_chrome():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    assert "Example" in driver.title
    sleep(2)
    driver.quit()