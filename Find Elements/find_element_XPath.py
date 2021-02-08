from selenium import webdriver

# from selenium.webdriver.firefox.webdriver import WebDriver
class findElementByXPath():
    
    def test(self):
        driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')
        driver.get("https://letskodeit.teachable.com/pages/practice")

        # finding element with Xpath
        elementByXPath = driver.find_element_by_xpath("//*[@id='name']")

        if elementByXPath:
            print("Found the Element with Xpath")

        # finding element by css Selector
        elementByCSS_selector = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS_selector:
            print("Found the element with Css selector")

runBrowser = findElementByXPath()
runBrowser.test()