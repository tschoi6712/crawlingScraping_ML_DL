# 1-11 네이버 금융에서 환율 정보 추출하기

from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출하기 --- (※1)
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)