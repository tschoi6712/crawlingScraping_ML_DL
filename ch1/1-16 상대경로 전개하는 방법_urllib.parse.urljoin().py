# 1-16 상대경로 전개하는 방법_urllib.parse.urljoin()

"""
1) 절대경로 : 어떠한 웹페이지나 파일이 가지고 있는 고유한 경로
2) 상대경로 : '현재 위치한 곳을 기준'으로 해서 '그곳의 위치'

  '/'   -> 가장 최상의 디렉토리로 이동(Web root)
  './'  -> 파일이 현재 디렉토리를 의미
  '../' -> 상위 디렉토리로 이동, 두단계 상위 디렉토리로 이동하려면 '../../' 

"""

from urllib.parse import urljoin

base = "http://example.com/html/a.html"

# URL을 기반으로 상대경로를 절대경로로 변환
print( urljoin(base, "b.html") )
print( urljoin(base, "sub/c.html") )
print( urljoin(base, "../index.html") )
print( urljoin(base, "../img/hoge.png") )
print( urljoin(base, "../css/hoge.css") )


print( urljoin(base, "/hoge.html") )
print( urljoin(base, "http://otherExample.com/wiki") )
print( urljoin(base, "//anotherExample.org/test") )