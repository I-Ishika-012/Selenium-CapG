from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Mobiles")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

noOfProducts = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

print(f"Total no of products - {len(noOfProducts)}")

for i in range(len(noOfProducts)):
    if i == 6:
        print(noOfProducts[i].text)

sixthProd = driver.find_element(By.XPATH, '//div[@data-component-type="s-search-result"][6]//div[@class="puisg-col-inner"]').click()

# driver.quit()