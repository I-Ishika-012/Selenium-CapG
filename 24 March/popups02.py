from time import sleep
from click import pause
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
#add below loc if download is blocked
opt.add_experimental_option("prefs", {
"safebrowsing.enabled": True
})
#to disable notifications
opt.add_argument("--disable-notifications")
driver = Chrome(options=opt)

driver.maximize_window()

# driver.get("https://demoqa.com/upload-download")
#
# upload = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
# sleep(2)
# upload.send_keys(r"C:\Users\Hp\Downloads\sampleFile.jpeg")
# download = driver.find_element(By.XPATH, "//a[@id='downloadButton']")
# download.click()

# driver.get("https://www.python.org/downloads/")
# download = driver.find_element(By.XPATH, "//a[.='Download Python install manager']")
# download.click()

driver.get("https://demoqa.com/automation-practice-form")