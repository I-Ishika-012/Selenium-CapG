from selenium.webdriver import Chrome, ChromeOptions
opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.get("https://www.wikipedia.org/")

driver.maximize_window()


print(driver.current_url)