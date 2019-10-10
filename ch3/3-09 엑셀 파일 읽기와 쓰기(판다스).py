# 3-09 엑셀 파일 읽기와 쓰기(판다스)

import pandas as pd

# 엑셀 파일 열기 --- (※1)
filename = "pop_stats_1041.xlsx" # 파일 이름
sheet_name = "sheet1" # 시트 이름
book = pd.read_excel(filename, sheet_name=sheet_name, header=1) # 첫 번째 줄부터 헤더

# 2017년 인구로 정렬 --- (※2)
book = book.sort_values(by=2017, ascending=False)
print(book)