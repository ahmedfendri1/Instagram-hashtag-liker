from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import time 
from time import sleep
from random import choice
import pyperclip
import random
from colorama import Fore, Back, Style
delay_time = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4]
import warnings
warnings.filterwarnings("ignore")

#Welcome Page
print("")
print("  _____           _                                    ____        _   ")
print(" |_   _|         | |                                  |  _ \      | |  ")
print("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ")
print("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|")
print("  _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ")
print(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|")
print("                            __/ |                                      ")
print("                           |___/                                       ")
print("# ==============================================================================")
print("# author       :Ahmed Fendri")
print("# github       :https://github.com/ahmedfendri1")
print("# date         :01.12.2021")
print("# version      :1.0")
print("# ==============================================================================")
print("")
print('This code is written by Tech World group')
print('Instagram liker by hastag')
print('Enter Username and password')
print('Enter the hastag and the number of likes')
print("# ==============================================================================")
chrome_options = Options()
'''chrome_options.add_argument("--test-type")'''
chrome_options.add_argument('--ignore-certificate-errors')
'''chrome_options.add_argument('--disable-extensions')'''
chrome_options.add_argument('disable-infobars')
'''chrome_options.add_argument("--incognito")'''
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--user-data=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=chrome_options)


driver.get("https://www.instagram.com/?hl=en")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
time.sleep(3)

lgn = 0
while lgn<1: 
    username = input("Enter Username:")
    time.sleep(1)
    password = input("Enter Password:")
    time.sleep(1)
    #username = 'joy_smile_laugh'
    for value1 in username:
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(value1)
        sleep(choice(delay_time))
    time.sleep(2)   
    for value2 in password:
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(value2)
        sleep(choice(delay_time))        
    time.sleep(3)    
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(6)
    lgn = 1    
    try: 
        if driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input'):
            lgn = 0 
            print('Please re-enter username and password')
            driver.get("https://www.instagram.com/?hl=en")
    except Exception:
        pass

try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
except Exception:
    pass
time.sleep(3)    
try:
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
except Exception:
    pass
time.sleep(2) 

lve = 0 
while lve < 1:
    hastag = input("Enter hastag:")
    time.sleep(1)
    driver.get('https://www.instagram.com/explore/tags/' + hastag) 
    #driver.get("https://www.instagram.com/explore/tags/likeforlikes/")
    time.sleep(5)  

    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(3) 
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div').click()
    time.sleep(5) 
    print('hint: limited number of likes is recommended (less than 300)')
    n_likes = int(input("Enter number of likes:"))
    time.sleep(1)                                             
    rn = random.randint(5,15)
    #n_likes = random.randint(100,300)
    for _ in range(n_likes):
        try:
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]').click()
        except Exception:                 
            pass
        time.sleep(rn)               
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button/div').click()
        time.sleep(3)                 
    print('done')
