from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wdw
from selenium.webdriver.support import expected_conditions as Ec
from random import randrange as rd
import csv
import time

url = 'https://flight.naver.com/'
browser = webdriver.Chrome('C:/j/chromedriver.exe')
browser.get(url)
browser.maximize_window() # 창을 최대 크기로 설정

filename = '네이버항공권.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # newline은 자동 줄바꿈을 없애주기 위해 사용
writer = csv.writer(f)

title = '항공사 이벤트혜택 출발시간 도착시간 소요시간 가격 카드혜택 혜택가격'.split()
# list 형태로 저장
writer.writerow(title)

def back():
    time.sleep(rd(t_min, t_max))
    browser.back()
    # print('뒤로')

def forward():
    time.sleep(rd(t_min, t_max))
    browser.forward()
    # print('앞으로')
    
def refresh():
    time.sleep(rd(t_min, t_max))
    browser.refresh()
    # print('새로 고침')
    
def input_click(ele):
    time.sleep(rd(t_min, t_max))
    ele.click()
    time.sleep(rd(t_min, t_max))
    # print('클릭')
    
def input_text(ele, text):
    time.sleep(rd(t_min, t_max))
    ele.click()
    ele.send_keys(text)
    ele.send_keys(Keys.RETURN)
    time.sleep(rd(t_min, t_max))
    # print('글자 입력')

# 항공편 정렬
def air_list_align(n):
    if n == 1:
        btn = browser.find_element(By.XPATH, '//span[contains(text(), "가격 낮은 순")]')
        input_click(btn)
    elif n == 2:
        btn = browser.find_element(By.XPATH, '//span[contains(text(), "가격 높은 순")]')
        input_click(btn)
    elif n == 3:
        btn = browser.find_element(By.XPATH, '//span[contains(text(), "출발시각 빠른 순")]')
        input_click(btn)
    elif n == 4:
        btn = browser.find_element(By.XPATH, '//span[contains(text(), "출발시각 늦은 순")]')
        input_click(btn)
    else:
        btn = browser.find_element(By.XPATH, '//span[contains(text(), "소요시간 짧은 순")]')
        input_click(btn)

# csv 파일 생성
def create_csv(rows, cols = 8):
    for content in rows:
        data = list(map(str, content.text.split('\n'))) # 텍스트로 가져오므로 \n을 기준으로 나누어 지므로 \n을 기준으로 잘라서 나눔
        if len(data) < cols: # 이벤트 혜택이 없는 경우 해당 col에 값 추가
            data.insert(1, '없음')
        writer.writerow(data)
    print('csv 파일 생성 완료')
    
t_min = 1
t_max = 2

departure = '김포'
arrival = '제주'
d_day = 10
a_day = 20
cost_order = 1 # 항공편 정렬 번호

# 날짜 선택
btn = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
input_click(btn)
day = browser.find_elements(By.XPATH, f'//b[text() = "{d_day}"]')
input_click(day[0]) # idx가 0이면 이번달
day = browser.find_elements(By.XPATH, f'//b[text() = "{a_day}"]')
input_click(day[0]) # idx가 0이면 이번달

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

order = Wdw(browser, 30).until(Ec.presence_of_element_located((By.XPATH, '//div[@class="domestic_sort__SjvyY"]')))
input_click(order)

# 항공편 정렬 선택
air_list_align(cost_order)

# 대기문, 해당 class 값을 가진 div가 나올 때 까지 30초 동안 대기
contents = Wdw(browser, 30).until(Ec.presence_of_all_elements_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
create_csv(contents)
browser.quit()

# while True:
#     pass