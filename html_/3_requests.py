import requests

res = requests.get("https://www.naver.com")
res.raise_for_status() # 문제가 생기면 바로 종료

res2 = requests.get("https://nadocoding.tistory.com")

# print('응답코드 : ', res.status_code) # 200 이면 정상
# print('응답코드 : ', res2.status_code)

if res.status_code == requests.codes.ok: # 200이랑 똑같은 뜻
    print('정상')
else:
    print('비정상')

print(len(res.text)) # 홈페이지 코드의 개수 출력
# print(res.text)

# with open('mygoogle.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)