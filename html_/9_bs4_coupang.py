# 쿠팡이 웹스크래핑을 막으므로 제대로된 작동이 되지 않아 g마켓을 이용

import requests
import re
from bs4 import BeautifulSoup as bs


url = 'http://browse.gmarket.co.kr/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&k=32&p=1'
# headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
res = requests.get(url)
res.raise_for_status() # 문제가 생기면 바로 종료
soup = bs(res.text, 'lxml')

# print('응답코드 : ', res.status_code) # 200 이면 정상
# print(soup)
# print('응답코드 : ', res2.status_code)



# 해당 내용의 모든 이름, 가격, 평점, 평점 수, 구매를 가져와 출력
content = soup.find_all('div', attrs={'class': "box__component box__component-itemcard box__component-itemcard--general"})


for l in range(len(content)):
    # 공식 제품만 출력되게
    official = content[l].find('span', attrs={'class': 'box__brand'})
    if official.find('span', attrs={'class': 'text'}):
        name = content[l].find('span', attrs={'class':'text__item'})
        price = content[l].find('strong', attrs={'class':'text text__value'})
        rate = content[l].find('li', attrs={'class':'list-item list-item__awards'})
        rate_cnt = content[l].find('li', attrs={'class':'list-item list-item__feedback-count'})
        buy_cnt = content[l].find('li', attrs={'class':'list-item list-item__pay-count'})
        
        print('이름: ' + name.get_text())
        print('가격: ' + price.get_text() + ' 원')
        print('평점: ' + (rate.get_text() if rate else '없음'))
        print('평점 수: ' + (rate_cnt.get_text() if rate_cnt else '상품평 (0)건'))
        print('구매: ' + (buy_cnt.get_text() if buy_cnt else '구매 0건'))
        print()
    
