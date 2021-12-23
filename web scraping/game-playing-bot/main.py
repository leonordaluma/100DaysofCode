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
# cookie = driver.find_element(By.ID, 'cookie')
# timeout = 60*1
# start = time.time()

# while True:
#     cookie.click()
#     delta = time.time() - start
#     if delta>= timeout:
#         break
    


driver.quit()
