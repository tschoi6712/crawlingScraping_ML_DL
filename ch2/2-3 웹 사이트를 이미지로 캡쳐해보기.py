# 2-3 웹 사이트를 이미지로 캡쳐해보기

## 웹 브라우저 원격조작에 사용하는 Selenium
## 화면 없는 웹 브라우저 "PhantomJS"

from selenium import webdriver
url = "https://www.naver.com/"

# PhantomJS 드라이버 추출하기 --- (※1)
browser = webdriver.PhantomJS("C:/phantomjs-2.1.1/bin/phantomjs.exe")

# 3초 대기하기 --- (※2)
browser.implicitly_wait(3)

# URL 읽어 들이기 --- (※3)
browser.get(url)

# 화면을 캡처해서 저장하기 --- (※4)
browser.save_screenshot("Website.png")

# 브라우저 종료하기 --- (※5)
browser.quit()