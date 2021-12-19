from selenium import webdriver

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
chromedriver_path = "../chromedriver.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

driver.get("https://www.amazon.com")
print(driver.title)
