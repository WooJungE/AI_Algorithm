#컴볼루션 신경망 코드
#Python과 TensorFlow 라이브러리를 사용하여 MNIST 숫자 이미지를 분류하는 Convolutional Neural Network(CNN) 구현

import tensorflow as tf

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# CNN 모델 구성
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D((2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(10)
])

# 모델 컴파일 및 학습
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train.reshape(-1, 28, 28, 1), y_train, epochs=5, validation_data=(x_test.reshape(-1, 28, 28, 1), y_test))

# 모델 평가
model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test, verbose=2)

# tf.keras.layers.Conv2D와 tf.keras.layers.MaxPooling2D를 사용하여 Convolutional Layer를 구성
# 그 후 tf.keras.layers.Flatten으로 평탄화를 수행하고, Fully Connected Layer에 대한 tf.keras.layers.Dense를 추가
# 이 모델은 tf.keras.models.Sequential로 구성됨

#모델을 컴파일하고 학습하기 위해 model.compile과 model.fit 함수를 사용
#마지막으로, 모델을 평가하기 위해 model.evaluate를 사용
