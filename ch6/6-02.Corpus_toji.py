# 6-02.Corpus_toji

# 말뭉치 데이터베이스 https://ithub.korean.go.kr/user/total/database/corpusManager.do

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

# utf-16 인코딩으로 파일을 열고 글자를 출력하기 --- (※1)
fp = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body > text")
text = body.getText()

# 텍스트를 한 줄씩 처리하기 --- (※2)
okt = Okt() 
word_dic = {}
lines = text.split("\r\n")

for line in lines:
    malist = okt.pos(line)
    for word in malist:
        if word[1] == "Noun": #  명사 확인하기 --- (※3)
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 카운트하기

# 많이 사용된 명사 출력하기 --- (※4)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()