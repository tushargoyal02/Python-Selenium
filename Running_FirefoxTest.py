from selenium import webdriver

# initite the driver instance
driver = webdriver.Firefox(executable_path=r'C:\Users\tusha\Documents\Selenium Python\geckodriver.exe')

# driver get {get: will help to open web application}
driver.get("https://youtube.com")