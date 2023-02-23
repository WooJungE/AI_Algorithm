# Scikit-learn 라이브러리를 사용하여 단순 선형 회귀 모델을 학습시키는 코드

from sklearn.linear_model import LinearRegression
import numpy as np

# 훈련 데이터 준비
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5]).reshape(-1, 1)

# 선형 회귀 모델 객체 생성
lr = LinearRegression()

# 모델 학습
lr.fit(X, y)

# 모델 학습 결과 출력
print("회귀 계수 w:", lr.coef_)
print("절편 b:", lr.intercept_)

# 1차원 입력 데이터와 해당 출력 데이터가 주어진 경우
     # Scikit-learn 라이브러리를 사용하여 단순 선형 회귀 모델을 학습하고 회귀 계수와 절편을 출력

# 모델을 학습시키는 과정
     # 1. 입력 데이터와 출력 데이터를 준비
          # 'reshape(-1, 1)' 메소드를 사용하여 1차원 배열을 2차원 배열로 변환
     # 2. 선형 회귀 모델 객체를 생성
     # 3. 'fit()' 메소드를 사용하여 모델을 학습
     # 4. 'coef_' 속성과 'intercept_' 속성을 사용하여 회귀 계수와 절편을 출력
      
# cikit-learn 라이브러리를 사용하여 선형 회귀 모델을 학습시키는 방법
# Scikit-learn 라이브러리를 사용하면 다차원 입력 데이터나 다양한 회귀 모델도 쉽게 학습시킬 수 있음
