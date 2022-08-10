import requests
from bs4 import BeautifulSoup as bs

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

# html을 lxml로 변환
soup = bs(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음으로 발견된 a element의 정보 출력
# print(soup.a.attrs) # a element의 속성 출력
# print(soup.a['href']) # a element의 href 속성 값 출력

# print(soup.find('a', attrs={'class':'Nbtn_upload'})) # class 값이 Nbtn_upload인 a element를 찾는다.
# print(soup.find(attrs={'class':'Nbtn_upload'})) # class 값이 Nbtn_upload인 element를 찾는다.

# print(soup.find('li', attrs={'class':'rank01'}))
# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a)
# print(rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text()) # 2등의 정보 출력

# rank2 = rank1.find_next_sibling('li') # rank1.next_sibling.next_sibling 과 같은 거
# print(rank2.a.get_text())

# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text()) # 3등의 정보 출력

# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling # 3등을 기준으로 2등으로 돌아감
# print(rank2.a.get_text())

# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# print(rank1.parent.get_text()) # 부모 출력

# print(rank1.find_next_siblings('li')) # 모든 형제들을 출력

webtoon = soup.find('a', text='이상한 변호사 우영우-3화: 이상한 변호사 우영우 (3)')
print(webtoon.get_text())