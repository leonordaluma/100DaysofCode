from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from account import username, password
from time import sleep

TWITTER_EMAIL = username
TWITTER_PASSWORD = password
CHROME_DRIVER_PATH = "../chromedriver.exe"
PROMISED_UP = 20.8
PROMISED_DOWN = 7.42

class InternetSpeedTwitterBot:
    def __init__(self):
        self.s = Service("../chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.down = 0
        self.up = 0
    
    
    def get_internet_speed(self):
        self.driver.implicitly_wait(260)
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go_button.click()        
        
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        print(f"down: {self.down.text}")
        print(f"up: {self.up.text}")
        # selenium waits
        self.driver.quit()
        
        
    
    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.get_internet_speed()
