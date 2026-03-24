"""
accessing elements within a frame:
-index -- method->switch_to_frame
(first "embedded" element is idx 0)
-name --give a name to iframe then pass it as arg in the mtd
-as web element itself --use xpath

switching bw frames:
--switch to parent frame to go to immediate parent frame
--switch to default content to go main/initial webpage
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

driver.maximize_window()

driver.get("http://127.0.0.1:5500/24%20March/page1.htm")

# #using id
# inp1 = driver.find_element(By.ID, "inputone")
# inp1.send_keys("First")
# sleep(1)
# driver.switch_to.frame(0)
# inp2 = driver.find_element(By.ID, "inputtwo")
# inp2.send_keys("Second")
# sleep(1)
# driver.switch_to.frame(0)
# inp3 = driver.find_element(By.ID, "inputthree")
# inp3.send_keys("Third")

#using name
# inp1 = driver.find_element(By.ID, "inputone")
# inp1.send_keys("First")
# sleep(1)
# driver.switch_to.frame("frame1")
# inp2 = driver.find_element(By.ID, "inputtwo")
# inp2.send_keys("Second")
# sleep(1)
# driver.switch_to.frame("frame2")
# inp3 = driver.find_element(By.ID, "inputthree")
# inp3.send_keys("Third")
# sleep(1)

#using web element itself
inp1 = driver.find_element(By.ID, "inputone")
inp1.send_keys("First")
sleep(1)
iframeOne = driver.find_element(By.XPATH, "//iframe[@id='frame1']")
driver.switch_to.frame(iframeOne)
inp2 = driver.find_element(By.ID, "inputtwo")
inp2.send_keys("Second")
sleep(1)
iframeTwo = driver.find_element(By.XPATH, "//iframe[@id='frame2']")
driver.switch_to.frame(iframeTwo)
inp3 = driver.find_element(By.ID, "inputthree")
inp3.send_keys("Third")
sleep(1)
driver.switch_to.default_content()
inp1.clear()
inp1.send_keys("I am Inevitable")
sleep(1)
