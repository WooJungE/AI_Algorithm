# Python에서 Scikit-learn 라이브러리를 사용하여 선형 회귀 모델을 학습 코드
# Scikit-learn은 Python에서 널리 사용되는 머신 러닝 라이브러리 중 하나

from sklearn.linear_model import LinearRegression
import numpy as np

# 훈련 데이터 준비
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 5, 4, 5])

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X_train, y_train)

# 새로운 데이터에 대해 예측
X_new = np.array([[6], [7]])
y_pred = model.predict(X_new)

# 예측 결과 출력
print(y_pred)

# 1차원 입력 데이터와 해당 출력 데이터가 주어진 경우
     # 단순 선형 회귀 모델을 학습하고 새로운 입력 데이터에 대한 예측 결과를 출력

# 모델은 Scikit-learn 라이브러리의 LinearRegression 클래스를 사용하여 만듦
# 모델을 학습시키기 위해 fit() 메서드를 호출
# 새로운 입력 데이터를 예측하기 위해 predict() 메서드를 호출
