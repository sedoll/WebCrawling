from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randrange as rd
import pyperclip
import time

url = 'https://flight.naver.com/'
browser = webdriver.Chrome('C:/j/chromedriver.exe')
browser.get(url)
browser.maximize_window()

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
    
def input_click(ele):
    time.sleep(rd(t_min, t_max))
    ele.click()
    time.sleep(rd(t_min, t_max))
    
def input_text(ele, text):
    time.sleep(rd(t_min, t_max))
    ele.click()
    ele.send_keys(text)
    ele.send_keys(Keys.RETURN)
    time.sleep(rd(t_min, t_max))
    
t_min = 1
t_max = 2

departure = '김포'
arrival = '제주'
d_day = 27
a_day = 30

# 날짜 선택
btn = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
input_click(btn)
day = browser.find_elements(By.XPATH, f'//b[text() = "{d_day}"]')
input_click(day[0])
day = browser.find_elements(By.XPATH, f'//b[text() = "{a_day}"]')
input_click(day[0])

# 출발지 선택
btn = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b')
input_click(btn)
text = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input')
input_text(text, departure)
btn = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]')
input_click(btn)

# 도착지 선택
btn = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b')
input_click(btn)
text = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input')
input_text(text, arrival)
btn = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]')
input_click(btn)

# 항공권 검색
btn = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button')
input_click(btn)

browser.implicitly_wait(15)

while True:
    pass