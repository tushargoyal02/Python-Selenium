from selenium import webdriver

# from selenium.webdriver.firefox.webdriver import WebDriver
class findElementByClass_Tag():
    
    def test(self):
        driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')
        driver.get("https://letskodeit.teachable.com/pages/practice")

        # finding element with ClassName
        elementByClassName = driver.find_element_by_class_name("displayed-class")

        if elementByClassName:
            print("Found the Element with Class Name")

        # finding element by Tag Name
        elementByTagName = driver.find_element_by_tag_name("a")

        if elementByTagName:
            print("Found the element with Tag Name")

runBrowser = findElementByClass_Tag()
runBrowser.test()