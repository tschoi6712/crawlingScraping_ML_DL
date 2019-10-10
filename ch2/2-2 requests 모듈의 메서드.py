# 2-2 requests 모듈의 메서드

"""
1) GET 요청
   req = requests.get("http://      ")
   
2) POST 요청
   formdata = {"키1":"값1", "키2":"값2"}
   req = requests.post("http://      ", data=formdata)
"""

## 예제1: 현재 시간을 제공하는 API

# 데이터 가져오기
import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

# 텍스트 형식으로 데이터 추출하기
text = r.text
print(text)

# 바이너리 형식으로 데이터 추출하기
bin = r.content
print(bin)


## 예제2: 바이너리 데이터인 이미지를 받아 저장

# 이미지 데이터 추출하기
import requests
r = requests.get("http://wikibook.co.kr/wikibook.png")

# 바이너리 형식으로 데이터 저장하기
with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")