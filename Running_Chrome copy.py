from selenium import webdriver

class IeRunner():

    def test(self):

        driverLocation=r'C:\Users\tusha\Documents\Selenium Python\IEDriverServer.exe'

        driver = webdriver.Ie(driverLocation)

        driver.get('https://regexsoftware.com')

# creating a object for the above class
runChrome = IeRunner()

# running the functions
runChrome.test()