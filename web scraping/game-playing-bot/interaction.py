from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# # article_count.click()

# article_link = driver.find_element(By.LINK_TEXT,"All portals")
# # article_link.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Leonor")
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Daluna")
email = driver.find_element(By.NAME, 'email')
email.send_keys("llll@gmail.com")
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()



# driver.quit()