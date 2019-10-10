# 1-4 매개변수를 추가해 요청을 전송하는 방법
"""
방식: GET(웹 브라우저에 주소 입력)
대상: http://(호스트 이름)/ (경로) ? (데이터지정: 키=값&키=값....)
"""

import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 자료형의 매개변수를 URL 인코딩합니다. --- (※1)
values = {'stnId': '108'}
params = urllib.parse.urlencode(values)

# 요청 전용 URL을 생성합니다. --- (※2)
url = API + "?" + params
print("url=", url)

# 다운로드합니다. --- (※3)
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)