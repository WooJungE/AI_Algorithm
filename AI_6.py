# 의사결정 나무(decision tree)는 데이터를 분류하는 분류기(classifier)로 사용
# 각 분기점마다 특정 조건에 따라 데이터를 분류하는 방식
# 데이터의 특성을 고려하여 최적의 분류 방식을 찾아내기 때문에 많은 분야에서 사용

# sklearn 라이브러리를 이용하여 의사결정 나무를 학습시키고 예측하는 코드

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 불러오기
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 분리하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 의사결정 나무 모델 학습시키기
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 예측하기
y_pred = clf.predict(X_test)

# 정확도 측정하기
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# sklearn 라이브러리에서 제공하는 붓꽃(iris) 데이터를 사용하여 의사결정 나무 모델을 학습
# 테스트 데이터에서 예측 결과의 정확도를 측정
# 각 특성(feature)에 따라 꽃의 종류를 분류하는 분류 문제 >>> 의사결정 나무 알고리즘이 적합한 선택
