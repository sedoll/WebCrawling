from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange as rd
import pyperclip
import time

def clipboard_input(user_xpath, user_input): # 아이디, 비밀번호를 입력받기 위한 함수
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        browser.find_element("xpath", user_xpath).click()
        ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(rd(t_min, t_max))
        

options = webdriver.ChromeOptions()
# options.headless = True # 웹페이지가 보이지 않고 프로그램 실행
# options.add_argument("winddow-size=1920x1080") # 웹페이지가 보이지 않고 프로그램 실행
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

# url = 'https://newslibrary.naver.com/search/searchByKeyword.naver#%7B%22mode%22%3A1%2C%22sort%22%3A0%2C%22trans%22%3A1%2C%22pageSize%22%3A10%2C%22keyword%22%3A%22%ED%83%9C%ED%92%8D%20%EC%95%A0%EA%B7%B8%EB%8B%88%EC%8A%A4%22%2C%22status%22%3A%22success%22%2C%22startIndex%22%3A1%2C%22page%22%3A1%2C%22startDate%22%3A%221920-03-05%22%2C%22endDate%22%3A%221999-12-31%22%7D'

name = input('주제를 입력하세요. > ')
pages = int(input('몇 페이지 까지 크롤링 하시겠습니까? > '))
p = 1
url = f'https://newslibrary.naver.com/search/searchDetails.naver#%7B%22mode%22%3A1%2C%22sort%22%3A0%2C%22trans%22%3A%221%22%2C%22pageSize%22%3A10%2C%22keyword%22%3A%22{name}%22%2C%22startDate%22%3A%221975-01-01%22%2C%22endDate%22%3A%221999-12-31%22%2C%22status%22%3A%22success%22%2C%22page%22%3A{p}%2C%22office%22%3A%22111111%22%2C%22pageno%22%3A%2210%22%2C%22section%22%3A%22111111111%22%2C%22type%22%3A%22111111111111111111111111111%22%2C%22scope%22%3A%2210%22%7D'
browser = webdriver.Chrome('C:/j/chromedriver.exe', options=options)
browser.get(url)

# 딜레이 시간
t_min = 3
t_max = 5
b_id = '네이버 아이디'
b_pw = '네이버 비빌번호'

# 아이디, 비밀번호 입력
clipboard_input('//*[@id="id"]', b_id)
clipboard_input('//*[@id="pw"]', b_pw)
browser.find_element(By.XPATH, '//*[@id="log.login"]').click()

if pages > 1:
    for page in range(p, pages+1):
        url = f'https://newslibrary.naver.com/search/searchDetails.naver#%7B%22mode%22%3A1%2C%22sort%22%3A0%2C%22trans%22%3A%221%22%2C%22pageSize%22%3A10%2C%22keyword%22%3A%22{name}%22%2C%22startDate%22%3A%221975-01-01%22%2C%22endDate%22%3A%221999-12-31%22%2C%22status%22%3A%22success%22%2C%22page%22%3A{page}%2C%22office%22%3A%22111111%22%2C%22pageno%22%3A%2210%22%2C%22section%22%3A%22111111111%22%2C%22type%22%3A%22111111111111111111111111111%22%2C%22scope%22%3A%2210%22%7D'
        browser.get(url)
        time.sleep(rd(t_min, t_max))
        contents = browser.find_elements(By.CLASS_NAME, 'data')
        print(str(page) + '페이지')
        for content in contents:
            print(content.text)
            print(content.find_element(By.TAG_NAME, 'a').get_attribute('href'))
            print()
else:
    time.sleep(rd(t_min, t_max))
    contents = browser.find_elements(By.CLASS_NAME, 'data')
    for content in contents:
        print(content.text)
        print(content.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        print()
browser.quit()