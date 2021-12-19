from selenium import webdriver

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
chromedriver_path = "../chromedriver.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)

driver.get("https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=sr_1_1_sspa?keywords=oculus&qid=1639825393")
print(driver.find_element_by("priceblock_ourprice"))
# print(driver.title)
driver.quit()