# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os 
import time
import ast

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
import atexit
#Accts = driver.find_elements(By.CLASS_NAME,'marketIndexItem--otherInfo')
def exit_handler():
    file=open("visited.txt","w")
    file.write(str(visited))
    file.close()
atexit.register(exit_handler)
#acc prob not needed as write to fiel on regular basis

if os.path.getsize('visited.txt') == 0:
    visited=set()
else:
    file=open("visited.txt","r")
    visited=ast.literal_eval(file.read())
    file.close()


def scanNewAccts():
    Accts = driver.find_elements(By.CLASS_NAME,'marketIndexItem.PopupItemLink.PopupItemLinkActive')
    print(Accts)
    print(Accts[0])
    print("a")
    for acct in Accts:
        
        #would be faster to use XPATH (XML) selector
        #not learning allat for now, no time
    
        topcontainer = acct.find_element(By.CLASS_NAME,"marketIndexItem--topContainer")
        insideh4 = topcontainer.find_element(By.TAG_NAME,"h4")
        atag = insideh4.find_element(By.CLASS_NAME,"marketIndexItem--Title.PopupItemLink")
        acctID = atag.get_attribute("href")
        #can also take acctID from Accts as a comparison base, maybe XPATH not faster
        #bc kinda slow #haha my laptop is just slow nvm it's fine
       

    
        inside = acct.find_element(By.CLASS_NAME,"marketIndexItem--otherInfo")
        seller = inside.text.split(" ")[0]
        timesinceposting = inside.text.split(" ")[1] + ' ' + inside.text.split(" ")[2]
        print(inside.text.split(" ")[0],inside.text.split(" ")[1],inside.text.split(" ")[2],acctID)

        if acctID in visited:
            pass
        else:
            visited.add(acctID)
            print("New account posted by", seller, timesinceposting, acctID)
        
        #then overwrite everything in visited set into visited.txt 
    

print("b")

while True:
    
    scanNewAccts()
    
    print("ITERATION \n")
    print(visited)

    time.sleep(30)