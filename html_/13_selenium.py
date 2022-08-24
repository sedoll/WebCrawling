from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randrange as rd
import pyperclip
import time

def back():
    time.sleep(rd(t_min, t_max))
    browser.back()
    print('뒤로')

def forward():
    time.sleep(rd(t_min, t_max))
    browser.forward()
    print('앞으로')
    
def refresh():
    time.sleep(rd(t_min, t_max))
    browser.refresh()
    print('새로 고침')
    
def input_button(ele, text):
    ele.click()
    time.sleep(rd(t_min, t_max))
    ele.send_keys(text)
    ele.send_keys(Keys.RETURN)
    
t_min = 3
t_max = 5

browser = webdriver.Chrome('C:/j/chromedriver.exe')
browser.get('https://www.naver.com')

btn = browser.find_element(By.CLASS_NAME, 'link_login') # 이메일 접속
# find_element 는 하나만 / find_elements 는 리스트 형태로 일치하는 것들을 가져옴
btn.click()

back()

input_text = browser.find_element(By.CLASS_NAME, 'input_text') # 검색창
input_button(input_text, '나도코딩')

while True:
    pass