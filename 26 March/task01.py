"""
--open pinterest
--full page screenshot
--scroll to elem
--elem screenshot
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

opt = ChromeOptions()
opt.add_experimental_option('detach', True)
driver = Chrome(options=opt)

