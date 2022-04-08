
# 웹통신을 위한 모듈 ==> requests
# html 을 분석하여 정보를 구조적으로 제공 ==> beautifulSoup
import requests as re
from bs4 import BeautifulSoup


# 사용법 : 가져오고싶은 html 문서 --> 주소를 가져옴

url = "https://www.naver.com"

res = re.get(url) #주소를 넘기면 해당 주소로 접속

print(res)
# [200]이 나오면 접속에 성공

html = res.text

# print(html)
soup = BeautifulSoup(html, 'html.parser') # html형식의 문자열을 넘기면 html 구조로 파싱(쪼개줌)


# list_theme_wrap type_topstory
# 
print("-"*50)
print(soup.select("div.sc_login a")) # 선택자를 이용해서 특정 영역 또는 태그를 선택.결과 한개여도 리스트로 반환

tags = soup.select("div.sc_login a")
atag = tags[0]

print(atag)

print(atag["href"]) # 태그의 속성



print("-"*50)

divs = soup.select("div.thumb_area div.thumb_box img")


print(divs[10])

div = divs[10]

print(div["alt"])


for div in divs :
    print(div["alt"])
    print(div["src"])


# 언론사별 top5 기사 [순위, 제목, 본문링크]를 리스트에 저장