# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discord_webhook import DiscordWebhook
import os 
import time
import ast


def launchBrowser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://lzt.market/steam/rust?hours_played[252490]=800&country[]=Canada&country[]=United%20States&mm_ban=nomatter&order_by=price_to_up")
    return driver

driver=launchBrowser()


while True:
    time.sleep(1)