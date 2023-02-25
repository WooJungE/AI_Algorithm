# 의사결정 나무 알고리즘은 데이터를 기반으로 결정 트리를 구성하여 분류 또는 회귀 문제를 해결하는 머신러닝 알고리즘

# scikit-learn 라이브러리를 이용한 의사결정 나무 알고리즘 코드

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# iris 데이터셋 불러오기
iris = load_iris()

# feature, target 데이터 지정
X = iris.data
y = iris.target

# train, test 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 의사결정 나무 모델 생성
clf = DecisionTreeClassifier()

# 모델 학습
clf.fit(X_train, y_train)

# 모델 예측
y_pred = clf.predict(X_test)

# 정확도 평가
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# scikit-learn 라이브러리에서 제공하는 iris 데이터셋을 사용하여 의사결정 나무 모델을 생성하고, 학습 및 평가를 수행
# 모델 생성 후, 'fit()' 함수를 사용하여 학습을 진행하고, 'predict()' 함수를 사용하여 예측 결과를 얻음
# 'accuracy_score()' 함수를 사용하여 모델의 정확도를 평가
