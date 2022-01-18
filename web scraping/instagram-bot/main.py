from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from credentials import username, password

CHROME_DRIVER_PATH = "../chromedriver.exe"
SIMILAR_ACCOUNT = ""
USERNAME = username
PASSWORD = password


class InstaFollower:
    def __init__(self):
         self.s = Service("../chromedriver.exe")
         self.driver = webdriver.Chrome(service=self.s)
    
    
    def login(self):
        self.driver.get("https://www.instagram.com/")
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(PASSWORD)
        password_input.send_keys()
    
    def find_followers(self):
        pass
    
    def follow(self):
        pass


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
