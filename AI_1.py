#선형 회귀 알고리즘은 가장 간단한 머신러닝 알고리즘 중 하나
#입력 데이터와 출력 데이터 간의 선형적인 관계를 찾아내는 알고리즘
#선형 회귀 모델의 핵심은 입력 데이터의 특성(feature)과 가중치(weight)를 곱해서 출력을 예측하는 것
#가중치를 학습을 통해 찾아내는 것이 핵심

import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
      
      
# NumPy를 사용하여 구현된 선형 회귀 알고리즘
#입력 데이터 X와 출력 데이터 y를 이용하여 모델을 학습
#predict() 메서드를 이용하여 새로운 입력 데이터에 대한 출력을 예측
#fit() 메서드는 경사 하강법(gradient descent)을 이용하여 가중치와 편향을 학습하는 것이 핵심

#위 코드는 기본적인 선형 회귀 알고리즘을 구현한 것
#입력 데이터 X와 출력 데이터 y는 적절한 전처리가 필요할 수 있음 >>> 구현에 반영해야 함
