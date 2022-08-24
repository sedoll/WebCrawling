from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import time
from random import randrange as rd

def clipboard_input(user_xpath, user_input): # 아이디, 비밀번호를 입력받기 위한 함수
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element("xpath", user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(rd(t_min, t_max))
        
def input_click(elem):
        time.sleep(rd(t_min, t_max))
        elem.click()
        
def input_text(elem, text):
        elem.click()
        time.sleep(rd(t_min, t_max))
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)

# 딜레이 시간
t_min = 3
t_max = 5

# 아이디, 비밀번호, 검색 내용
b_id = 'id'
b_pw = 'pw'
content = 'it'

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('C:\\j\\chromedriver.exe', options=options)
driver.get('https://naver.com')
driver.implicitly_wait(15) # 페이지가 로딩 될때 까지 최대 10초 기다림
print('로그인 진행중...')

# 로그인 ---------------------------------------
btn= driver.find_element(By.CLASS_NAME, 'link_login') # 이메일 접속
btn.click()

# 아이디, 비밀번호 입력
clipboard_input('//*[@id="id"]', b_id)
clipboard_input('//*[@id="pw"]', b_pw)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# time.sleep(5)
driver.implicitly_wait(15)

# ----------------------------------------------

# 블로그 ----------------------------------------
btn = driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[3]/a') # 블로그 접속
input_click(btn)

btn = driver.find_elements(By.TAG_NAME, 'a')[3] # 검색
input_click(btn)

btn = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/input') # 블로그 접속
input_text(btn, content)
# inputbox = driver.find_elements(By.CLASS_NAME, 'input_text__Sr51l')[0]
# inputbox.click()
# inputbox.send_keys('it')
# inputbox.send_keys(Keys.RETURN)
# inputbox = driver.find_elements(By.TAG_NAME, 'input')[0]
# clipboard_input('//*[@id="root"]//div[1]//div//form//input', content)
# inputbox.send_keys(Keys.RETURN)

# ----------------------------------------------

# insta_tag = "travel"
# like_cnt = 100
# driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
# time.sleep(5)
# driver.implicitly_wait(15)

# new_feed = driver.find_elements(By.XPATH, '//article//img //ancestor :: div[2]')[9]
# new_feed.click()

# numoflike = 0
# for i in range(like_cnt): 
#     driver.implicitly_wait(15)
#     span = driver.find_element(By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]')  
#     like_btn = span.find_element(By.TAG_NAME, 'button')
#     btn_svg = like_btn.find_element(By.TAG_NAME, 'svg') 
#     svg = btn_svg.get_attribute('aria-label') 
    
#     if svg == '좋아요' : 
#         like_btn.click() 
#         numoflike += 1
#         print('좋아요를 {}번째 눌렀습니다.'.format(numoflike))
#         time.sleep(random.randrange(50,60))
#     else :
#         print('이미 작업한 피드입니다.')               
#         time.sleep(random.randrange(5))        

#     if i < like_cnt-1 : 
#         next_feed_xpath = driver.find_element(By.XPATH, '//*[@aria-label="다음" and @height="16"]//ancestor :: div[2]')
#         next_feed = next_feed_xpath.find_element(By.TAG_NAME, 
#     'button') 
#         next_feed.click() 
#         driver.implicitly_wait(15)

# while True: # 화면 꺼짐 방지
#       pass

# print("좋아요 작업이 끝났습니다. 프로그램을 종료합니다.")
# driver.quit()

while True:
        pass