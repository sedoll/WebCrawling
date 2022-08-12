import requests
from bs4 import BeautifulSoup as bs

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

# html을 lxml로 변환
soup = bs(res.text, 'lxml')

with open('webtoon.html', 'w', encoding='UTF-8') as f:
    f.write(res.text)
# 조건에 해당하는 모든걸 가져옴
# cartoons = soup.find_all('a', attrs={'class': 'title'})
# # class 속성이 title인 모든 'a' element를 반환
# for cartoon in cartoons:
#     print(cartoon.get_text())
# with open('webtoon.txt', 'w', encoding='UTF-8') as f:
#     f.write(soup.get_text())
