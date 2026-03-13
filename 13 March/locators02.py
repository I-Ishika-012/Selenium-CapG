from time import sleep

from selenium.webdriver.common.by import By


from selenium.webdriver import Chrome, ChromeOptions
opt=ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

#eg: amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
search=driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("men's jeans")
sleep(2)
#USING ID
btn=driver.find_element(By.ID, "nav-search-submit-button")

#USING NAME
# btn=driver.find_element(By.NAME, "field-keywords")

#USING CLASS
# btn=driver.find_element(By.CLASS_NAME, "nav-input.nav-progressive-attribute") #do not forget to use . in place of space in case of compound class



btn.click()
sleep(2)

#using link
lnk = driver.find_element(By.LINK_TEXT, "Amazon Pay")
lnk.click()

sleep(2)
'''
href="/flights?ref_=apay_deskhome_Flights"
'''
#USING CSS SELECTORS
fly=driver.find_element(By.CSS_SELECTOR, 'a[href="/flights?ref_=apay_deskhome_Flights"]')
fly.click()
