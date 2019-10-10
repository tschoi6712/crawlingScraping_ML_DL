#1-1 urllib.request를 이용한 다운로드

import urllib.request

# URL과 저장 경로 지정하기  --- (※1)
url = "https://d1.awsstatic.com/diagrams/product-page-diagrams/Diagram_ai-category_machine-learning-workflow.89d4ebdfb4159dfc70b4eff6027eca4ca59ccaec.png"
savename = "ai_test.png"

# 다운로드(파일로 저장) --- (※2)
urllib.request.urlretrieve(url, savename)

print("저장되었습니다...!")