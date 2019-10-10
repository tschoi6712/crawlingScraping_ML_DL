# 5-09.tensorboard_BMI2

import pandas as pd
import numpy as np
import tensorflow as tf

# 키, 몸무게, 레이블이 적힌 CSV 파일 읽어 들이기 --- (※1)
csv = pd.read_csv("bmi.csv")

# 데이터 정규화 --- (※2)
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

# 레이블을 배열로 변환하기 --- (※3)
# - thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))

# 테스트를 위한 데이터 분류 --- (※4)
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

# 데이터 플로우 그래프 구축하기 --- (※5)

# 플레이스홀더 선언하고 이름 붙이기
x  = tf.placeholder(tf.float32, [None, 2], name="x") # 키와 몸무게 데이터 넣기
y_ = tf.placeholder(tf.float32, [None, 3], name="y_") # 정답 레이블 넣기

# interface 부분을 name_scope로 묶기
with tf.name_scope('interface') as scope:
    # 변수 선언하고 이름 붙이기 --- (※6)
    W = tf.Variable(tf.zeros([2, 3]), name="W"); # 가중치
    b = tf.Variable(tf.zeros([3]), name="b"); # 바이어스
    
    # 소프트맥스 회귀 정의하기 --- (※7)
    with tf.name_scope('softmax') as scope:
        y = tf.nn.softmax(tf.matmul(x, W) + b)

# loss 계산을 name_scope로 묶기(오차함수) --- (※8)
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# training 계산을 name_scope로 묶기(경사하강법)
with tf.name_scope('training') as scope:
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

# accuracy 계산을 name_scope로 묶기
with tf.name_scope('accuracy') as scope:
    predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))


# 세션 시작하기 --- (※9)
with tf.Session() as sess:   
    sess.run(tf.global_variables_initializer()) # 변수 초기화하기

    # TensorBoard 사용하기 --- (※)
    tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

    # 학습시키기
    for step in range(3500):
        i = (step * 100) % 14000
        rows = csv[1 + i : 1 + i + 100]
        x_pat = rows[["weight","height"]]
        y_ans = list(rows["label_pat"])
        fd = {x: x_pat, y_: y_ans}
        sess.run(train, feed_dict=fd)
        if step % 500 == 0:
            cre = sess.run(cross_entropy, feed_dict=fd)
            acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
            print("step=", step, "cre=", cre, "acc=", acc)

    # 최종적인 정답률 구하기
    acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
    print("정답률 =", acc)

