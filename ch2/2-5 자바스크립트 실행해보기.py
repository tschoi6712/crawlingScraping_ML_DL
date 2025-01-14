# 2-5 자바스크립트 실행해보기

from selenium import webdriver

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS("C:/phantomjs-2.1.1/bin/phantomjs.exe")
browser.implicitly_wait(3)

# 적당한 웹 페이지 열기
browser.get("https://google.com")

# 자바스크립트 실행하기
r = browser.execute_script("return 100 + 50")
print(r)