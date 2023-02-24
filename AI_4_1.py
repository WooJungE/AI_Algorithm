#Scikit-learn 라이브러리를 사용하여 선형 회귀 모델을 학습시키는 코드

from sklearn.linear_model import LinearRegression

# 훈련 데이터 준비
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 5, 4, 5]

# 선형 회귀 모델 객체 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 모델 학습 결과 출력
print("회귀 계수 w:", model.coef_)
print("절편 b:", model.intercept_)

# 1차원 입력 데이터와 해당 출력 데이터가 주어진 경우
     # Scikit-learn 라이브러리를 사용하여 선형 회귀 모델을 학습하고 회귀 계수와 절편을 출력
  
# 모델을 학습시키는 과정
     # 입력 데이터와 출력 데이터를 준비
     # 선형 회귀 모델 객체를 생성
     # 모델을 학습
     # 회귀 계수와 절편을 출력
    
# Scikit-learn 라이브러리는 다양한 회귀 모델과 성능 평가 지표를 제공하며 다차원 입력 데이터와 다중 출력 데이터의 경우에도 적용 가능
     # 따라서 이 방법을 사용하는 것이 일반적
