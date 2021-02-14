from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select

class DropDown_usingSelect():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        
        driverLocation=r'C:\Users\tusha\Documents\Selenium Python\chromedriver.exe'
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(10)

        # Finding the elements then selecting it
        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        # selecting someting with value
        print("Taking up [Benz] Value from drop -down")
        sel.select_by_value("benz")

        time.sleep(2)

        # ----- Selecting Honda By index ---
        sel.select_by_index("2")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        time.sleep(2)

obj = DropDown_usingSelect()
obj.test()

