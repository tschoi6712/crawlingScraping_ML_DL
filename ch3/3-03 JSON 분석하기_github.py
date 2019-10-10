# 3-03 JSON 분석하기_github

"""
자바스크립트에서 사용하는 객체 표기 방법
1) 숫자
2) 문자열 "str"
3) 불 true, false
4) 배열 [n1, n2, n3, ....]
5) 객체 {"키":값, ....}
6) null
# JSON 데이터를 파이썬으로 == json.loads()
# 파이썬 으로 생성한 데이터를 JSON으로 == json.dumps()

"""

import urllib.request as req
import os.path, random
import json

# JSON 데이터 내려받기 --- (※1)
url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(url):
    req.urlretrieve(url, savename)

# JSON 파일 분석하기 --- (※2)
items = json.load(open(savename, "r", encoding="utf-8"))

# s = open(savename, "r", encoding="utf-8").read()
# items = json.loads(s)

# 출력하기 --- (※3)
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])