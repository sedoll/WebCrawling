import requests
import re
from bs4 import BeautifulSoup as bs

# 원하는 연도의 top5 영화 포스터 추출
for year in range(2020, 2022):
    url = f'https://search.daum.net/search?w=tot&q={year}년영화순위&DA=MOR&rtmaxcoll=MOR'
    res = requests.get(url)
    res.raise_for_status() # 문제가 생기면 바로 종료
    soup = bs(res.text, 'lxml')
    images = soup.find_all('img', attrs={'class' : 'thumb_img'})

    for idx, image in enumerate(images):
        image_url = image['src']
        if 'R232x328' in image_url: # 영화 포스터 크기만 적용되 있는 사진 추출
            print(image_url)
        try:
            image_res = requests.get(image_url)
            image_res.raise_for_status()
            
            with open('movie_{}_{}.jpg'.format(year, idx+1), 'wb') as f:
                f.write(image_res.content) # 리소스 정보를 파일로 사용
        except Exception as e:
            break 
        
        if idx >= 4: # 상위 5개의 이미지만 다운
            break
