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
        frame = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.switch_to.frame(frame)
        username_input = self.driver.find_element(By.XPATH, )
        username_input.send_keys(USERNAME)
        # password.send_keys(PASSWORD)
    
    def find_followers(self):
        pass
    
    def follow(self):
        pass


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
