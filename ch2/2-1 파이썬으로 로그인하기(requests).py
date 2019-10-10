# 2-1 파이썬으로 로그인하기(requests)

"""
1) HTTP 통신 : 브라우저에서 서버로 요청(request)하고, 서버에서 브라우저로 응답(response)할 때 규약
2) 쿠키는 브라우저를 통해 사이트를 방문한 사람의 데이터를 일시적으로 저장(세션ID)하고, 세션은 이를 기반으로 
   데이터 파일을 만들고 변수 의 값을 저장
"""

# 로그인을 위한 모듈 추출하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정하기 --- (※1)
USER = "tschoi67"
PASS = "Ts003998"

# 세션 시작하기 --- (※2)
session = requests.session()

# 로그인하기 --- (※3)
login_info = {
    "m_id": USER,  # 아이디 지정
    "m_passwd": PASS  # 비밀번호 지정
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외가 발생합니다.

# 마이페이지에 접근하기 --- (※4)
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html" 
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기 --- (※5)
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()

print("마일리지: " + mileage)
print("이코인: " + ecoin)