# 코스피 시가총액 추출

import requests
import re
import csv
from bs4 import BeautifulSoup as bs

filename = '공주대 게시판 안내.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # newline은 자동 줄바꿈을 없애주기 위해 사용
writer = csv.writer(f)

try:
    for sel in (range(12499, 12503)):
        url = f'https://www.kongju.ac.kr/kongju/{sel}/subview.do'
        res = requests.get(url)
        res.raise_for_status()
        soup = bs(res.text, 'lxml')
        
        sub = soup.find('h2').get_text().split(',')
        writer.writerow(sub)
        
        title = '번호 제목 작성자 작성일 조회 파일 링크'.split()
        writer.writerow(title)
        
        data_rows = soup.find('table', attrs={'class': 'board-table horizon1'}).find('tbody').find_all('tr')
        for idx, data_row in enumerate(data_rows):
            columns = data_row.find_all('td')
            url2 = data_row.find('td', attrs={'class': 'td-subject'}).find('a')['href'] # 링크 추출
            if idx > 4:
                writer.writerow('')
                break
            data = [column.get_text().strip() for column in columns]
            data.append('https://www.kongju.ac.kr/' + url2) # 링크
            writer.writerow(data)
        print(str(sub) + 'csv 파일 생성 완료')
except Exception:
    print('실행 오류')