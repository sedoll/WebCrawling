# 정규식
import re

# 차량번호 4개의 문자
# abcd, book, desk
# ca?e
# care, cafe, case, cave

p = re.compile('ca.e') # 원하는 정규식 형태로 컴파일
# . (ca.e) : 하나의 문자를 의미 > care, cafe
# ^ (^de) : 문자열의 시작을 의미 > desk, destination
# $ (se$) : 문자열의 끝 > case, base

def print_match(m):
    if m:
        print('m.group(): ', m.group()) # 일치하는 문자열 반환
        print('m.string: ', m.string) # 입력받은 문자열 반환
        print('m.start(): ', m.start()) # 일치하는 문자열의 시작 인덱스
        print('m.end(): ', m.end()) # 일치하는 문자열의 끝 인덱스
        print('m.span(): ', m.span()) # 일치하는 문자열의 시작과 끝을 표시
        print()
    else:
        print('매칭되지 않음')
        
# m = p.match('careless') # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

m = p.search('careless') # search : 주어진 문자열 중에 일치하는지 확인
print_match(m)

m = p.search('good care') # search : 주어진 문자열 중에 일치하는지 확인
print_match(m)

lst = p.findall('good care cafe') # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)