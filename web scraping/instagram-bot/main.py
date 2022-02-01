from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credentials import username, password
import time

CHROME_DRIVER_PATH = "../chromedriver.exe"
SIMILAR_ACCOUNT = "slickspicymemes"
USERNAME = username
PASSWORD = password


class InstaFollower:
    def __init__(self):
        self.s = Service("../chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)

    def login(self):
        # self.driver.find_element(By.LINK_TEXT, 'Log In').click()
        self.driver.get('https://www.instagram.com/')
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element(By.CSS_SELECTOR, '.sqdOP .yWX7d .y3zKF').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.aOOlW .HoLwm ').click()
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        
        

    def find_followers(self):
        pass

    def follow(self):
        pass


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
