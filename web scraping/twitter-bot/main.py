from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 20.8
PROMISED_UP = 7.42
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)