# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def launchBrowser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://lzt.market/telegram/?order_by=pdate_to_down_upload")
    return driver

driver=launchBrowser()

notRobot = driver.find_element(By.CSS_SELECTOR,"body > div > form > button")
notRobot.click()

ruski = driver.find_element(By.CSS_SELECTOR,"#content > div > div > div.mainContainer > div > div.FloatingContainer.Notices > div > div > div > a")
ruski.click()
time.sleep(3)
Accts = driver.find_elements(By.CLASS_NAME,'marketIndexItem--otherInfo')

print(Accts)
print(Accts[0])
print("a")

# print(Accts[0].get_attribute('textContent').strip())
for acct in Accts:
    print(acct.text.split(" ")[0])

print("b")

while True:
    time.sleep(1)
    