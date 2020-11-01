import time
import datetime
import sys
from selenium import webdriver
from kavenegar import *

def sendMessage(link,title):
    api = KavenegarAPI('31666C573963674A714E706E31655A786D4E4B66417776304F61787A3771334B563536515842485356446B3D')
    response = api.sms_send( params = { 'sender' : '1000596446', 'receptor': '09146501380', 'message' :title+"\n"+link })
    print("Message Sent")
    time.sleep(10)


lastLink="http://www.sanjesh.org/FullStory.aspx?gid=1&id=6824"
retryTime=10

while True:
    browser = webdriver.Chrome(sys.path[0]+'\\chromedriver.exe')
    browser.get('http://www.sanjesh.org/group.aspx?gid=1');
    currentLink=browser.find_element_by_xpath("//*[@id='bodyLeft']/div/div[4]/div/ul/li[1]/a").get_attribute("href")
    currentTitle=browser.find_element_by_xpath("//*[@id='bodyLeft']/div/div[4]/div/ul/li[1]/a").text
    browser.quit()
    print("Checked at "+datetime.datetime.now().time().strftime("%H:%M:%S"))
    if currentLink!=lastLink:
        print("New Title Has Been Added.")
        sendMessage(currentLink,currentTitle)
        lastLink=currentLink
        print("Checking Again In "+str(retryTime)+" Minutes.")
    else:
        print("No Update. Trying Again In "+str(retryTime)+" Minutes.")
    time.sleep(retryTime*60)
