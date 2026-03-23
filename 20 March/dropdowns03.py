from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.zomato.com/jaipur/restaurants")
sleep(2)
wait = WebDriverWait(driver, 10)
search = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder,'Search')]"))
)

search.click()
search.send_keys("Momos")

# 🔥 wait for ANY suggestion text to appear
suggestions = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//p[contains(text(),'Momos')]")
    )
)

# print all suggestions
for s in suggestions:
    print(s.text)

# 🔥 click "Momos Wala"
target = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//p[text()='Momos Wala']")
    )
)

driver.execute_script("arguments[0].click();", target)



# click matching suggestion
# for s in suggestions:
#     if "Momos" in s.text:
#         driver.execute_script("arguments[0].click();", s)
#         break