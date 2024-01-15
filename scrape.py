# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



# def launchBrowser():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get("https://reddit.com")
#     return driver

# driver=launchBrowser()
# elem = driver.find_element(By.CSS_SELECTOR, "#login-button > span > span")
#driver.find_elements


def launchBrowser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://google.com")
    return driver

driver=launchBrowser()
elem = driver.find_element(By.CSS_SELECTOR, "#gb > div > div:nth-child(1) > div > div:nth-child(1) > a")
# elem.click()

print(elem)


x=1
while True:
    print(x,elem.get_attribute("href"))
    x+=1


#marketItem--91502858 > div.marketIndexItem--topContainer > h4 > a > div > div
    
#for a search element, like a text box
    #u can use searchelement.send_keys("string")

    #what happens if the element doesn't exist?

driver.back()
driver.forward()
driver.refresh()
driver.quit()
#$copy link from searchbar
#or find a link from inside a button
#driver.getCurrentUrl() 
#https://stackoverflow.com/questions/67502946/find-the-url-after-button-click-from-the-website-using-selenium-python