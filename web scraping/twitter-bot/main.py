# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from account import username, password

# TWITTER_EMAIL = username
# TWITTER_PASSWORD = password
# CHROME_DRIVER_PATH = "../chromedriver.exe"
# PROMISED_UP = 20.8
# PROMISED_DOWN = 7.42


# class InternetSpeedTwitterBot:
#     def __init__(self):
#         self.s = Service("../chromedriver.exe")
#         self.driver = webdriver.Chrome(service=self.s)
#         self.down = 0
#         self.up = 0

#     def get_internet_speed(self):
#         self.driver.get("https://www.speedtest.net/")
#         go_button = self.driver.find_element(
#             By.CSS_SELECTOR, '.start-button a')
#         go_button.click()

#         upload_speed_locator = (
#             By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

#         WebDriverWait(self.driver, 180).until(
#             EC.text_to_be_present_in_element(upload_speed_locator, "."),
#             "test didn't complete.(or spend more the 3 minute)"
#         )
#         self.down = self.driver.find_element(
#             By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
#         self.up = self.driver.find_element(
#             By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

#         print(f"down: {self.down}")
#         print(f"up: {self.up}")
#         self.driver.quit()

#     def tweet_at_provider(self):
#         self.driver.get("https://twitter.com/")
#         twitter_signin = self.driver.find_element(By.LINK_TEXT, 'Sign in')
#         twitter_signin.click()
#         input_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
#         input_field.click()
#         input_field.send_keys(TWITTER_EMAIL)


# bot = InternetSpeedTwitterBot()
# # bot.get_internet_speed()
# bot.tweet_at_provider()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from account import username, password
import time

TWITTER_URL = "https://twitter.com/"
SPEED_TEST_URL = "https://www.speedtest.net/"
CHROME_DRIVER_PATH = "../chromedriver.exe"
TWITTER_USERNAME = username
TWITTER_EMAIL = "leonordaluma"
TWITTER_PASSWORD = password


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.ser = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.PROMISED_DOWN = 150
        self.PROMISED_UP = 10

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)

        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a').click()
        except Exception as error:
            pass

        self.down_speed_result = self.driver.find_element(By.XPATH,
                                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up_speed_result = self.driver.find_element(By.XPATH,
                                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        return float(self.down_speed_result)

    def tweet_at_provider(self):
        tweet = f"Hey I just checked my internet speed from speedtest.net and my results are: {self.down_speed_result} Mbps/Down and {self.up_speed_result} Mpbs/Up."
        self.driver.get(TWITTER_URL)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(
            TWITTER_EMAIL)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]').click()
        time.sleep(2)
        # If Twitter asks for your username/phone (due to abnormal account activity) use these commands to enter your username (you may also change it to your phone instead)
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(
                TWITTER_USERNAME)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
        except Exception as error:
            pass

        time.sleep(2)
        # Use this command to login with your password if your username/phone was prompt in the previous step
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(
                TWITTER_PASSWORD)
        except Exception as error:
            pass

        # Use this command to login with your password if your Twitter did not prompt for your username/phone
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(
                TWITTER_PASSWORD)
        except Exception as error:
            pass

        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
        time.sleep(3)

        # Use this command to click on the updated TOS window once you successfully logged in.
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div').click()
        except Exception as error:
            pass

        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(
            tweet)

        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
if bot.get_internet_speed() < bot.PROMISED_DOWN:
    bot.tweet_at_provider()
