# 서포트 벡터 머신(Support Vector Machine, SVM)은 지도 학습(Supervised Learning) 알고리즘 중 하나
# 분류(Classification) 및 회귀(Regression) 분석에 사용
# Python에서 scikit-learn 라이브러리를 사용하여 SVM을 구현

# SVM을 사용한 이진 분류(binary classification) 코드

# 필요한 라이브러리 불러오기
from sklearn import svm
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 데이터 생성
X, y = make_blobs(n_samples=50, centers=2, random_state=6)

# SVM 모델 생성
clf = svm.SVC(kernel='linear', C=1000)

# 모델 학습
clf.fit(X, y)

# 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# 결정 경계(Decision Boundary) 그리기
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 모델로부터 w, b 값을 가져오기
w = clf.coef_[0]
b = clf.intercept_[0]

# 결정 경계 그리기
x1 = np.linspace(xlim[0], xlim[1], 20)
y1 = (-w[0] * x1 - b) / w[1]
plt.plot(x1, y1, '-k')

# 서포트 벡터 그리기
margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
y2 = y1 + margin
plt.plot(x1, y2, 'k--')

y3 = y1 - margin
plt.plot(x1, y3, 'k--')

plt.show()

# make_blobs 함수를 사용하여 데이터를 생성하고, 선형 SVM 모델을 학습한 후, 결과를 시각화
# 결정 경계(Decision Boundary)와 서포트 벡터(Support Vector)를 그리는 부분 포함
# 코드에서 사용된 kernel='linear'는 선형 커널(linear kernel)을 사용하겠다는 의미
# C=1000은 오분류를 얼마나 허용할 것인지에 대한 하이퍼파라미터로 값이 높을수록 오분류를 허용하지 않음
