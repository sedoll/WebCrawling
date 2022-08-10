import requests

res = requests.get("https://www.naver.com/")
res.raise_for_status() # 문제가 생기면 바로 종료

with open('naver.html', 'w', encoding='utf-8') as f:
    f.write(res.text)