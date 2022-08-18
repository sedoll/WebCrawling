# 코스피 시가총액 추출

import requests
import re
import csv
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

filename = '시가총액1-200.csv'
f = open(filename, 'w', encoding='utf-8', newline='') # newline은 자동 줄바꿈을 없애주기 위해 사용
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
# list 형태로 저장
writer.writerow(title)

try:
    for page in range(1, 2):
        res = requests.get(url + str(page))
        res.raise_for_status()
        soup = bs(res.text, 'lxml')
        
        data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
        for data_row in data_rows:
            columns = data_row.find_all('td')
            if len(columns) <= 1: # td가 한 개 이하인 경우는 추출하지 않음
                continue
            data = [column.get_text().strip() for column in columns]
            # print(data)
            writer.writerow(data)
    print('csv 파일 생성 완료')
except Exception:
    print('실행 오류')