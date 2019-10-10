#1-3 웹에서 데이터 추출하기

import urllib.request

url = "https://www.google.com/"
mem = urllib.request.urlopen(url).read()
print(mem.decode("euc-kr"))


# IP 확인 API로 접근해서 결과 출력하기

import urllib.request

# url을 호출하여 데이터 읽어 들이기 --- (※1)
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리를 문자열로 변환하기 --- (※2)
text = data.decode("utf-8")
print(text)