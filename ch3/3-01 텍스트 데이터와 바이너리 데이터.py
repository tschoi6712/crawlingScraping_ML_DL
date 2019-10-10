# 3-1 텍스트 데이터와 바이너리 데이터
"""
1) 텍스트 데이터 : 어떤 문자인코딩 인지 따라 다른 의미(utf-8, euc-kr)
2) 바이너리 데이터 : 이미지, 동영상
"""

# 파일 이름과 데이터
filename = "a.bin"
data = 100

# 쓰기
with open(filename, "wb") as f:
    f.write(bytearray([data]))