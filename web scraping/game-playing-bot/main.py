from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
item_store = driver.find_elements(By.CSS_SELECTOR, '#store div')
items_id = [i.get_attribute("id") for i in item_store]
cookie = driver.find_element(By.ID, 'cookie')
timeout = time.time() + 5
stop_loop = time.time() + 60 * 2
start = time.time()
        
all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
upgrade_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in all_prices if price.text != ""]
cookie_upgrades = {}
for i in range(len(upgrade_prices)):
    cookie_upgrades[upgrade_prices[i]] = items_id[i]

def buy_upgrades():
    cookie_money = driver.find_element(By.ID, 'money').text
    if "," in cookie_money:
        cookie_money = cookie_money.replace(",", "")
    numberOfCookies = int(cookie_money)
    
    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if numberOfCookies > cost:
            affordable_upgrades[cost] = id
    
    highest_price_affordable = max(affordable_upgrades)
    highest_price_id = affordable_upgrades[highest_price_affordable]
    driver.find_element(By.ID, highest_price_id).click()

while True:
    cookie.click()
    
    if time.time() >= timeout:
        buy_upgrades() 
        timeout = time.time() + 5
        
    if time.time() > stop_loop:
        cookie_per_s = driver.find_element(By.ID, 'cps')
        print(f"cookies/sec: {cookie_per_s.text}")
        break

driver.quit()
