# 첫번째 언론사 top5 기사 [순위, 제목, 본문링크]를 리스트에 저장
# 1. 출력
# 순위 : 1
# 제목 : 
# 본문링크 : 


# 2. 가능하다면 엑셀에 저장


import requests as re
from bs4 import BeautifulSoup

# 신원정보를 직접 입력할 수 있음
# User agent

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    
}

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"

res = re.get(url, headers = header)

# print(res)
html = res.text
soup = BeautifulSoup(html, 'html.parser')


print("-"*50)
# strongs = soup.select("div._officeCard0 div strong.rankingnews_name") # 아이디선택 -->#사용

# divs = soup.select("div._officeCard0 div")
# div = divs.select("strong.rankingnews_name")
# new_title = soup.select("div.list_content a")
# print(news[0])
# print(strongs[0])
atags = soup.select("div.list_content a")
for a in atags :
    title = a.text
    link = a["href"]
    print("제목 : {}".format(title))
    print("제목 : {}".format(link))
    print("-----")

# new_link = soup.select("div.list_content a.href")

