from selenium import webdriver
import time

class ChromeRunner():

    def test(self):

        driverLocation=r'C:\Users\tusha\Documents\Selenium Python\chromedriver.exe'

        driver = webdriver.Chrome(driverLocation)

        # maximize window size
        driver.maximize_window()

        # opening the url
        driver.get('http://www.grocerybagjaipur.in/')

        # getting the title from the webpage
        title_data = driver.title
        print(title_data)

        # getting the current Url
        current_url = driver.current_url
        print("Current working url is: ", current_url)

        time.sleep(5)

        # refresh the browser
        driver.refresh()    #driver.refresh(current_url)

        time.sleep(5)

        # Going back to the url
        driver.get('https://www.google.com')
        driver.back()

        # moving forward
        driver.forward()


        # get the page source
        ##pageSource = driver.page_source 

        # closing the Browser
        driver.quit()

driverRunner = ChromeRunner()

driverRunner.test()