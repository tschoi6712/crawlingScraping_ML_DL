# 5-08 텐서보드로 시각화(덧셈)

import tensorflow as tf

# 상수와 변수 선언하기 --- (※1)
a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

# 덧셈을 수행하는 그래프 정의하기 --- (※2)
calc_op = a + b * c 
assign_op = tf.assign(v, calc_op)

# 세션 생성하기 --- (※3)
sess = tf.Session()

# TensorBoard 사용하기 --- (※4)
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# 세션 실행하기  --- (※5)
sess.run(assign_op)
print(sess.run(v))