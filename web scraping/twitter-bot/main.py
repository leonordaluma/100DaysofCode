from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from account import username, password

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
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(
            By.CSS_SELECTOR, '.start-button a')
        go_button.click()

        upload_speed_locator = (
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

        WebDriverWait(self.driver, 180).until(
            EC.text_to_be_present_in_element(upload_speed_locator, "."),
            "test didn't complete.(or spend more the 3 minute)"
        )
        self.down = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f"down: {self.down}")
        print(f"up: {self.up}")
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        input_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]')
        input_field.click()
        


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
