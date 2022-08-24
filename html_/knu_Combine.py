# 공주대 공지사항 스크래핑

import requests
import csv
from bs4 import BeautifulSoup as bs

filename = '학교 학과 공지사항 스크래핑.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # newline은 자동 줄바꿈을 없애주기 위해 사용
writer = csv.writer(f)

# 학과 게시판
writer.writerow('학과공지사항')
try:
    for sel in (range(11607, 11610)):
        url = f'https://computer.kongju.ac.kr/ZD1140/{sel}/subview.do'
        res = requests.get(url)
        res.raise_for_status()
        soup = bs(res.text, 'lxml')
        
        sub = soup.find('h2', attrs={'class', 'on'}).get_text().split(',')
        writer.writerow(sub)
        
        title = '번호 제목 작성자 작성일 조회 파일 링크'.split()
        writer.writerow(title)
        
        data_rows = soup.find('table').find('tbody').find_all('tr', attrs={'class': ''})
        for idx, data_row in enumerate(data_rows):
            columns = data_row.find_all('td')
            url2 = data_row.find('td', attrs={'class': 'td-subject'}).find('a')['href'] # 링크 추출
            if idx > 4:
                writer.writerow('')
                break
            data = [column.get_text().strip() for column in columns]
            data.append('https://www.kongju.ac.kr/' + url2) # 링크
            writer.writerow(data)
        print('학과 공지사항' + str(sub) +' 스크래핑 완료')
except Exception:
    print('실행 오류')

# 학교 게시판
writer.writerow('학교공지사항')
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
        print('학교 공지사항' + str(sub) +' 스크래핑 완료')
except Exception:
    print('실행 오류')