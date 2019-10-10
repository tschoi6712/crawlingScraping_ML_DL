# 6-01.Konlpy_basic

# 1) KoNLPy 한국어 처리 패키지
import warnings
warnings.simplefilter("ignore")

import konlpy
konlpy.__version__

# 2) 한국어 말뭉치(헌법)
from konlpy.corpus import kolaw
kolaw.fileids()
c = kolaw.open('constitution.txt').read()
print(c[:200])

# 3) 형태소 분석
from konlpy.tag import *

hannanum = Hannanum() # 한나눔
kkma = Kkma()         # 꼬꼬마
komoran = Komoran()   # 코모란
#mecab = Mecab()       # 메카브(윈도우 X)
okt = Okt()           # 트위터형태소분석기(과거)

# nouns : 명사 추출
okt.nouns(c[:1000])

# morphs : 형태소 추출
okt.morphs(c[:1000])

# pos : 품사 부착
okt.pos(c[:1000])

# 품사 태그의 기호와 의미
okt.tagset

# 형태소 데이터프레임
import pandas as pd

tagsets = pd.DataFrame()
N = 67
tagsets["Hannanum-기호"] = list(hannanum.tagset.keys()) + list("*" * (N - len(hannanum.tagset)))
tagsets["Hannanum-품사"] = list(hannanum.tagset.values()) + list("*" * (N - len(hannanum.tagset)))
tagsets["Kkma-기호"] = list(kkma.tagset.keys()) + list("*" * (N - len(kkma.tagset)))
tagsets["Kkma-품사"] = list(kkma.tagset.values()) + list("*" * (N - len(kkma.tagset)))
tagsets["Komoran-기호"] = list(komoran.tagset.keys()) + list("*" * (N - len(komoran.tagset)))
tagsets["Komoran-품사"] = list(komoran.tagset.values()) + list("*" * (N - len(komoran.tagset)))
#tagsets["Mecab-기호"] = list(mecab.tagset.keys()) + list("*" * (N - len(mecab.tagset)))
#tagsets["Mecab-품사"] = list(mecab.tagset.values()) + list("*" * (N - len(mecab.tagset)))
tagsets["OKT-기호"] = list(okt.tagset.keys()) + list("*" * (N - len(okt.tagset)))
tagsets["OKT-품사"] = list(okt.tagset.values()) + list("*" * (N - len(okt.tagset)))
tagsets

# 자연어처리 패키지
import matplotlib.pylab as plt
from nltk import Text

kolaw = Text(okt.nouns(c), name="kolaw")
kolaw.plot(30)
plt.show()

# 워드클라우드 그리기
from wordcloud import WordCloud

# 한글 폰트 경로를 설정
#font_path = '/fonts/truetype/nanum/NanumGothic.ttf'
#wc = WordCloud(width = 1000, height = 600, background_color="white", font_path=font_path)

wc = WordCloud(width = 1000, height = 600, background_color="white")
plt.imshow(wc.generate_from_frequencies(kolaw.vocab()))
plt.axis("off")
plt.show()

