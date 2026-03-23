"""
dropdowns:
-select -- html select
-custom -- list . div, etc

select - single and  multi select dropdowns
-visible text
-by index -- 0 BASED
-by value
>>deselect unavailable

multiselect - select or deselect multiple dropdowns
same way as selecting in select
deselct also has same options + additional deselect all

"""
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get(r"file:C:\Users\Hp\Downloads\E22_Dropdowns.html")
sleep(2)
dropdown = driver.find_element(By.ID, "state")
select = Select(dropdown)
# select.select_by_visible_text("Bihar")
# select.select_by_value("MH")
# select.select_by_index(1)
multi = driver.find_element(By.ID, "hobby")
slct = Select(multi)
slct.select_by_index(0)
sleep(2)
slct.deselect_by_index(0)
sleep(2)
slct.select_by_visible_text("Yoga")
sleep(2)
slct.deselect_by_visible_text("Yoga")
sleep(2)
slct.select_by_value("music")
sleep(2)
slct.select_by_index(4)
sleep(2)
slct.deselect_all()
sleep(2)
driver.quit()