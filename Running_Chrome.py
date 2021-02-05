from selenium import webdriver

class ChromeRunner():

    def test(self):

        driverLocation=r'C:\Users\tusha\Documents\Selenium Python\chromedriver.exe'

        driver = webdriver.Chrome(driverLocation)

        driver.get('https://regexsoftware.com')

# creating a object for the above class
runChrome = ChromeRunner()

# running the functions
runChrome.test()