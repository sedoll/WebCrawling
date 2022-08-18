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


for l in content:
    
    name = l.find('span', attrs={'class':'text__item'}) # 이름
    if '그램' in str(name): # 이유는 모르겠지만 str로 안 묶어주면 처리가 안됨
        print('lg그램 제외\n') # lg그램 상품만 제외
        continue
    
    price = l.find('strong', attrs={'class':'text text__value'}) # 가격
    
    rate = l.find('li', attrs={'class':'list-item list-item__awards'}) # 평점
    if rate:
        rate = rate.get_text()
        # rate = rate[4:-6]
        rate = re.sub(r'[^0-9]', '', rate) # 숫자만 출력
    else:
        rate = '0'
        
    rate_cnt = l.find('li', attrs={'class':'list-item list-item__feedback-count'}) # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        # rate_cnt = rate_cnt[4:-2]
        rate_cnt = re.sub(r'[^0-9]', '', rate_cnt) # 숫자만 출력
    else:
        rate_cnt = '0'
        
    buy_cnt = l.find('li', attrs={'class':'list-item list-item__pay-count'}) # 구매
    if buy_cnt:
        buy_cnt = buy_cnt.get_text()
        # buy_cnt = buy_cnt[3:-1]
        buy_cnt = re.sub(r'[^0-9]', '', buy_cnt) # 숫자만 출력
    else:
        buy_cnt = '0'
    
    # if(int(rate) >= 90 and int(rate_cnt) >= 100 and int(buy_cnt) >= 300): # 평점이 90 이상이고 평점 수가 100개 이상인 제품만 출력
    
    print('이름: ' + name.get_text())
    print('가격: ' + price.get_text() + ' 원')
    print('평점: ' + rate + ' 점')
    print('평점 수: ' + rate_cnt + ' 개')
    print('판매량 : ' + buy_cnt + ' 개')
    print()
    
