# 4-07 MNIST-손글씨 숫자 데이터 학습시키기 

from sklearn import model_selection, svm, metrics

# CSV 파일을 읽어 들이고 가공하기 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

# 학습하기 --- (※2)
clf = svm.SVC(gamma='auto')
clf.fit(data["images"], data["labels"])

# 예측하기 --- (※3)
predict = clf.predict(test["images"])

# 결과 확인하기 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("보고서 : \n", cl_report)
