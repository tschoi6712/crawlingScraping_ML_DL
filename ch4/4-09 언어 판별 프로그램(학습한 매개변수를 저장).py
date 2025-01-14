# 4-09 언어 판별 프로그램(학습한 매개변수를 저장)

from sklearn import svm 
from sklearn.externals import joblib
import json

# 각 언어의 출현 빈도 데이터(JSON) 읽어 들이기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# 데이터 학습하기
clf = svm.SVC(gamma='auto')
clf.fit(data["freqs"], data["labels"])

# 학습 데이터 저장하기
joblib.dump(clf, "./lang/freq.pkl")
print("ok")