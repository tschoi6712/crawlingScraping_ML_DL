# 1-12 위키문헌에서 윤동주 작가의 작품 목록 가져오기

from bs4 import BeautifulSoup 
import urllib.request as req

# 위키 문헌 해당 페이지에 들어간 뒤에 주소를 복사해서 사용
url = "https://ko.m.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #mw-content-text 아래에  
# ul 태그 아래에  li 태그 아래에 있는 a 태그를 모두 선택합니다.
a_list = soup.select("#mw-content-text > div > ul > li a")
for a in a_list:
    name = a.string
    print("-", name)