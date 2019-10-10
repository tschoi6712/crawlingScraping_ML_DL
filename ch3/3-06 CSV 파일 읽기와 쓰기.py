# 3-06 CSV 파일 읽기와 쓰기

## 단순한 CSV 파일 읽기
import codecs
# EUC_KR로 저장된 CSV 파일 읽기(`codecs.open` 으로 인코딩을 지정)
filename = "list-euckr.csv"
csv = codecs.open(filename, "r", "euc_kr").read()

# CSV을 파이썬 리스트로 변환하기
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

# 결과 출력하기
for c in data:
    print(c[1], c[2])


## CSV 모듈 사용하기(csv.reader)

import csv, codecs
# CSV 파일 열기
filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr")

# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])


## CSV 파일 쓰기
import csv, codecs    
with codecs.open("test.csv", "w", "euc_kr ") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "SD 카드 ", 30000])
    writer.writerow(["1001", "키보드", 21000])
    writer.writerow(["1002", "마우스", 15000])