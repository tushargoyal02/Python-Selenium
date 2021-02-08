from selenium import webdriver

# from selenium.webdriver.firefox.webdriver import WebDriver
class findElementByXPath():
    
    def test(self):
        driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')
        driver.get("https://letskodeit.teachable.com/pages/practice")

        # finding element with LinkText
        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText:
            print("Found the Element with Link Text")

        # finding element by css Selector
        elementByPartial_textLink = driver.find_element_by_partial_link_text("Pra")

        print(elementByPartial_textLink)
        if elementByPartial_textLink:
            print("Found the element with Partial Text Link")

runBrowser = findElementByXPath()
runBrowser.test()