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
# buy_cursor = driver.find_element(By.ID, 'buyCursor')
# buy_grandma = driver.find_element(By.ID, 'buyGrandma')
# buy_factory = driver.find_element(By.ID, 'buyFactory')
# buy_mine = driver.find_element(By.ID, 'buyMine')
# buy_shipment = driver.find_element(By.ID, 'buyShipment')
# buy_alchemy_lab = driver.find_element(By.ID, 'buyAlchemy lab')
# buy_portal = driver.find_element(By.ID, 'buyPortal')
# buy_time_machine = driver.find_element(By.ID, 'buyTime machine')
cookie = driver.find_element(By.ID, 'cookie')
timeout = 60*1
start = time.time()

while True:
    cookie.click()
    delta = time.time() - start
    if delta>= timeout:
        break
    


driver.quit()
