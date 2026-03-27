from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/apparel-shoes")

driver.implicitly_wait(100)

def test_orderBy():
    orderby = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
    option1 = Select(orderby)
    option1.select_by_visible_text("Price: High to Low")

def test_pageSize():
    page = driver.find_element(By.XPATH, '//select[@id="products-pagesize"]')
    option2 = Select(page)
    option2.select_by_visible_text("12")

def test_viewMode():
    view = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
    option3 = Select(view)
    option3.select_by_visible_text("List")

sleep(5)
driver.quit()