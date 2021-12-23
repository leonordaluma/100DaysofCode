from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_money = driver.find_element(By.ID, 'money')
numberOfCookies = int(cookie_money.text)


item_store = driver.find_elements(By.CSS_SELECTOR, '#store div')
items_id = [i.get_attribute("id") for i in item_store]
cookie = driver.find_element(By.ID, 'cookie')
timeout = time.time() + 5
stop_loop = time.time() + 60
start = time.time()


all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
for price in all_prices:
    elements = price.text
    if elements != "":
        cost = int(price.text.split("-")[1].strip().replace(",", ""))
        print(cost)
# def upgrade_tag():
#     all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b moni')

# while True:
#     cookie.click()
    
#     if time.time() >= timeout:
        
    
#         timeout = time.time() + 5
    
#     if time.time() > stop_loop:
#         cookie_per_s = driver.find_element(By.ID, 'cps')
#         print(cookie_per_s.text)
#         break
    


driver.quit()
