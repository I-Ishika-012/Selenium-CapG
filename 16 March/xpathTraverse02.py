"""
traverse using sibling xpat:

following sibling--
//tag[attr="sometext"]//following-sibling::tag[index]

preceding sibling
//tag[attr="sometext"]//preceding-sibling::tag[index]
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
  
opt = ChromeOptions()
opt.add_argument("--headless") #use --headless to not open browser everytime
driver = Chrome(options=opt)

driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH, '//td[text()="Tim"]/following-sibling::td[2]')
print(due.text)

