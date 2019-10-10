# 1-8 DOM 요소의 속성에 대해

from bs4 import BeautifulSoup 
soup = BeautifulSoup(\
       "<p><a href='a.html'>test</a></p>", 'html.parser')

# 분석이 제대로 됐는 확인하기 --- (※1)
soup.prettify()

# <a>태그를 변수 a에 할당하고 attrs 속성의 자료형 확인하기 --- (※2)
a = soup.p.a
type(a.attrs)

# href 속성이 있는지 그리고 속성값 확인하기 --- (※3)
'href' in a.attrs
a['href']
