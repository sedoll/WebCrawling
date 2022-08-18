from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randrange as rd
import pyperclip
import time

def back():
    time.sleep(rd(3, 7))
    browser.back()
    print('뒤로')

def forward():
    time.sleep(rd(3, 7))
    browser.forward()
    print('앞으로')
    
def refresh():
    time.sleep(rd(3, 7))
    browser.refresh()
    print('새로 고침')

browser = webdriver.Chrome('C:/j/chromedriver.exe')
browser.get('https://www.naver.com')

btn = browser.find_elements(By.CLASS_NAME, 'link_login')[0] # 이메일 접속

btn.click()

back()

input_text = browser.find_elements(By.CLASS_NAME, 'input_text')[0] # 검색창
input_text.click()
input_text.send_keys('나도 코딩')
input_text.send_keys(Keys.RETURN)

while True:
    pass