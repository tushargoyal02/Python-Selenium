from selenium import webdriver
from selenium.webdriver.common.by import By

class ByFindElement():
    
    def test(self):
        driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')
        driver.get("https://letskodeit.teachable.com/pages/practice")

        # finding element with Id
        elementById = driver.find_element(By.ID, "name")


        # finding element with Xpath
        elementByXPath = driver.find_element(By.XPATH,"//*[@id='name']")

        if elementByXPath:
            print("Found the Element with Xpath")

        # finding element with Link Text
        elementByTextLink = driver.find_element(By.LINK_TEXT, "Login")



runBrowser = findElementByXPath()
runBrowser.test()