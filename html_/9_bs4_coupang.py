import requests
from bs4 import BeautifulSoup as bs

# hdr = {'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36'}
# url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=5&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
# res = requests.get(url, headers=hdr)
# res.raise_for_status()
# soup = bs(res.text, 'lxml')
# print(res.text)

# bs=BeautifulSoup(html, "html.parser")
# tag=(bs.html.title)

url = 'https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81'
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
res = requests.get(url)
res.raise_for_status() # 문제가 생기면 바로 종료
soup = bs(res.text, 'lxml')

print('응답코드 : ', res.status_code) # 200 이면 정상
print(soup)
# print('응답코드 : ', res2.status_code)
