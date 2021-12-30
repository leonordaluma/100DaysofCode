from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../chromedriver.exe"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.s = Service("../chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.promised_down = 20.8
        self.promised_up = 7.42
    
    
    def get_internet_speed(self):
        pass
    
    def tweet_at_provider(self):
        pass