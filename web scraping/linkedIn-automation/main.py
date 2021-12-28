import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credentials import ACCOUNT_EMAIL, ACCOUNT_PASSWORD

EMAIL = ACCOUNT_EMAIL
PASSWORD = ACCOUNT_PASSWORD

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
signin_btn = driver.find_element(By.LINK_TEXT, 'Sign in')
signin_btn.click()

username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
username_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

job_listings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
for listing in job_listings:
    print("called")
    listing.click()
    
    apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
    apply_btn.click()
    
    
    close_btn = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
    close_btn.click()
    
    discard_btn = driver.find_element(By.ID, 'ember367')
    discard_btn.click()
# apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
# apply_btn.click()

# next_btn = driver.find_element(By.CSS_SELECTOR, 'footer button')
# next_btn.click()
driver.quit()
