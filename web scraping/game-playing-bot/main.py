from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
# price = driver.find_element_by("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar) #selenium element
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_elements_by_class_name("python-logo")
# print(logo.size)

# docs_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(docs_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


date = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.last li time')
events = driver.find_elements(By.CSS_SELECTOR, '..most-recent-events li a')
for e in events:
    print(e.text)


python_events = {}
# python_events_dict = {index: val for index in range(len(date))}
for index in range(len(date)):
    python_events[index]
    python_events[index]["time"] = {d.text for d in date}
    python_events[index]["name"] = {e.text for e in events}

print(python_events)
    





driver.quit()