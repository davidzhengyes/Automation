# selenium 4

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discord_webhook import DiscordWebhook
import json
import os 
import time
import ast
from seleniumbase import SB


    
file = open('lztparams.json')
data=json.load(file)

refreshSeconds = data["frequency_seconds"]
discordTag = data["userID"]
webhookLink = data["DISCORD_WEBHOOK_URL"]
lztlink = data["lzt_page"]

if os.path.getsize('visited.txt') == 0:
    visited=set()
else:
    file=open("visited.txt","r")
    visited=ast.literal_eval(file.read())
    file.close()


def scanNewAccts():
    WebDriverWait(sb, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#title > div > span"))).click()
    resetbtn = sb.driver.find_element(By.CSS_SELECTOR,"#title > div > span")
    resetbtn.click()
    time.sleep(2)
    Accts = sb.find_elements(By.CLASS_NAME,'marketIndexItem.PopupItemLink.PopupItemLinkActive')
    print(Accts)
  

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
            print("AAAAAAAAAA SAW THIS ACC ALREADY")
        else:
            visited.add(acctID)
            msg="New account posted by"+ seller + timesinceposting + acctID + discordTag
            webhook = DiscordWebhook(url=webhookLink, content=msg)
            response = webhook.execute()
        file=open("visited.txt","w")
        file.write(str(visited))
        file.close()
        #then overwrite everything in visited set into visited.txt 
    
with SB(uc=True) as sb:
    sb.driver.uc_open_with_reconnect(
        lztlink ,
        reconnect_time=30
    )

    print("DRIVER RECON")
    while True:
    
        scanNewAccts()
        
        print("ITERATION \n")
        print(visited)

        time.sleep(int(refreshSeconds))

print("b")

