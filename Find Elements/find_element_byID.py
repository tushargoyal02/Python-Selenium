from selenium import webdriver

# from selenium.webdriver.firefox.webdriver import WebDriver

class findElementByID():
    
    def test(self):
        driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')

        driver.get("https://letskodeit.teachable.com/pages/practice")

        # finding the element by Id
        elementId = driver.find_element_by_id("name")
        if elementId:
            print("Found the Element with id")

        # element with the name
        elementByName = driver.find_element_by_name("show-hide")
        if elementByName:
            print("Found the element with name")

runBrowser = findElementByID()

runBrowser.test()