import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TWITTER = "https://twitter.com/login"
EMAIL = {Your email adress}
USERNAME = {Your username}
PASSWORD = {Your password}
SPEEDTEST = "https://www.speedtest.net/"
PROMISE_DOWN = 150
PROMISE_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISE_DOWN
        self.up = PROMISE_UP

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST)
        self.driver.find_element(
            "css selector", ".start-button a"
        ).click()  # Classe i tag
        time.sleep(60)
        self.download = self.driver.find_element(
            "xpath",
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        self.upload = self.driver.find_element(
            "xpath",
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text
        print(f"Down: {self.download}")
        print(f"Up: {self.upload}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER)
        time.sleep(5)
        email = self.driver.find_element(
            "xpath",
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        username = self.driver.find_element(
            "xpath",
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input',
        )
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(
            "xpath",
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        text = self.driver.find_element(
            "xpath", '//div[@data-testid="tweetTextarea_0"]'
        )
        message = f"Current download speed: {self.download} Mbs\nCurrent upload speed: {self.upload} Mbs"
        text.send_keys(message)
        self.driver.find_element(
            "xpath", '//div[@data-testid="tweetButtonInline"]'
        ).click()

# Create a instance and call both methods
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
