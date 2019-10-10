# 4-02 XOR 연산 학습(프레임워크)

import pandas as pd
from sklearn import svm, metrics

# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
xor_df = pd.DataFrame(xor_input)
xor_data  = xor_df.loc[:,0:1] # 데이터
xor_label = xor_df.loc[:,2]   # 레이블

#xor_data  = xor_df.ix[:,0:1] # 데이터
#xor_label = xor_df.ix[:,2]   # 레이블
"""
DeprecationWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
"""

# 데이터 학습과 예측하기 --- (※2)
clf = svm.SVC(gamma='auto')
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기 --- (※3)
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)