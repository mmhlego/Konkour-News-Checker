import time
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

def sendMessage(link):
    message="Link To The Title: "+link;
    browser = webdriver.Chrome(sys.path[0]+'\\chromedriver.exe')
    browser.get("https://accounts.google.com/signin/v2/identifier");
    email = browser.find_element_by_id('identifierId')
    email.click()
    email.send_keys("mmhlego@gmail.com")
    email.send_keys(Keys.ENTER)
    time.sleep(10)
    actions = ActionChains(browser)
    actions.send_keys("mohmah@8073"+Keys.ENTER)
    actions.perform()
    time.sleep(10)
    browser.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(10)
    browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()
    time.sleep(10)
    pyautogui.typewrite("mmhlego@gmail.com")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.typewrite("New Title Detected")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(message)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(10)
    browser.quit()

lastLink=""

while True:
    browser = webdriver.Chrome(sys.path[0]+'\\chromedriver.exe')
    browser.get('http://www.sanjesh.org/group.aspx?gid=1');
    currentLink=browser.find_element_by_xpath("//*[@id='bodyLeft']/div/div[4]/div/ul/li[1]/a").get_attribute("href")
    browser.quit()

    if currentLink!=lastLink:
        print("New Title Has Been Added.")
        sendMessage(currentLink)
        lastLink=currentLink
        print("Checking Again In 30 Minutes.")
    else:
        print("No Update. Trying Again In 30 Minutes.")
    time.sleep(1800)
