import requests
from bs4 import BeautifulSoup as bs

url = 'https://comic.naver.com/webtoon/weekday'
# url = 'https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu'
res = requests.get(url)
res.raise_for_status()

web = 'https://comic.naver.com'

soup = bs(res.text, 'lxml')
# cartoons = soup.find_all('td', attrs={'class': 'title'})
# title = cartoons[1].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print(web+link)

# 웹툰의 제목과 링크 출력
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a['href']
#     print(title)
#     print(web+link)

# 평균 평점 계산
# cartoons = soup.find_all('div', attrs={'class': 'rating_type'})
# rank = []
# for cartoon in cartoons:
#     value = float(cartoon.strong.get_text())
#     rank.append(value)
#     print(value)
# print('전체 점수: {:.2f}'.format(sum(rank)))
# print('평균 점수: {:.2f}'.format(sum(rank) / len(rank)))

cartoons = soup.find_all('a', attrs={'class': 'title'})
for cartoon in cartoons:
    print(cartoon.get_text())