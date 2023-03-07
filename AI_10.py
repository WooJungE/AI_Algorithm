# 컴볼루션 신경망(Convolutional Neural Network, CNN)은 이미지 인식과 같은 컴퓨터 비전 태스크에 자주 사용됨
# TensorFlow에서 컴볼루션 신경망을 구현하는 코드

import tensorflow as tf

# 입력 이미지와 레이블을 위한 플레이스홀더 생성
x = tf.placeholder(tf.float32, [None, 28, 28, 1])
y_ = tf.placeholder(tf.float32, [None, 10])

# 첫 번째 컨볼루션 레이어 생성
W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))
h_conv1 = tf.nn.relu(tf.nn.conv2d(x, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)

# 첫 번째 풀링 레이어 생성
h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# 두 번째 컨볼루션 레이어 생성
W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))
h_conv2 = tf.nn.relu(tf.nn.conv2d(h_pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)

# 두 번째 풀링 레이어 생성
h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# 완전 연결 레이어 생성
W_fc1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 드롭아웃 레이어 생성
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 출력 레이어 생성
W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# 손실 함수와 최적화 알고리즘 설정
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# 정확도 평가를 위한 연산 추가
correct_prediction
