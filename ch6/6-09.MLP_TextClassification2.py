# 6-09.MLP_TextClassification2

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import json

max_words = 67395 # 입력 단어 수: word-dic.json 파일 참고
nb_classes = 9    # 9개의 카테고리
batch_size = 32 
nb_epoch = 20

# MLP 모델 생성하기 --- (※1)
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    return model

# 데이터 읽어 들이기--- (※2)
root_dir = "D:/1.Workspace/1.Python_ws/2_3.MachineDeepLearningPython/News_text"
#data = json.load(open(root_dir + "/data-mini.json")) 
data = json.load(open(root_dir + "/data.json"))

X = data["X"] # 텍스트를 나타내는 데이터
Y = data["Y"] # 카테고리 데이터

# 학습하기 --- (※3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train),len(Y_train))
"""
1.Sequential 모형 클래스 객체 생성
2.add 메서드로 레이어 추가.
    입력단부터 순차적으로 추가한다.
    레이어는 출력 뉴런 갯수를 첫번째 인수로 받는다.
    최초의 레이어는 input_dim 인수로 입력 크기를 설정해야 한다.
    activation 인수로 활성화함수 설정
3.compile 메서드로 모형 완성.
    loss인수로 비용함수 설정
    optimizer 인수로 최적화 알고리즘 설정
    metrics 인수로 트레이닝 단계에서 기록할 성능 기준 설정
4.fit 메서드로 트레이닝
    nb_epoch 로 에포크(epoch) 횟수 설정
    batch_size 로 배치크기(batch size) 설정
    verbose는 학습 중 출력되는 문구를 설정 : 주피터노트북(Jupyter Notebook)을 사용은 verbose=2
"""
model = KerasClassifier(build_fn=build_model, nb_epoch=nb_epoch, batch_size=batch_size)
model.fit(X_train, Y_train)

# 예측하기 --- (※4)
y = model.predict(X_test)
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)