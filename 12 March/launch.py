# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome()
# sleep(10)
from time import sleep
from webbrowser import Chrome

from selenium.webdriver import Chrome, ChromeOptions
opt = ChromeOptions()
opt.add_experimental_option("detach", True) #holds screen
driver = Chrome(options=opt)

#fetch a website
driver.get("https://demoqa.com/")

#maximize a window
driver.maximize_window()

# driver.minimize_window()

#no taskbar/ title bar
# driver.fullscreen_window()

title = driver.title
print(title)

print(driver.current_url)

print(driver.name)

sleep(6)
# driver.close()

driver.quit()

#print(driver.page_source)