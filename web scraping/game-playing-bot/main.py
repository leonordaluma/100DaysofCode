from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_money = driver.find_element(By.ID, 'money')
cookies = int(cookie_money.text)
print(cookies)
print(type(cookies))


driver.quit()
