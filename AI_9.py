# 기본적인 인공 신경망의 예시인 다층 퍼셉트론(MLP)의 구현 코드

import numpy as np

# 시그모이드 함수 구현
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 다층 퍼셉트론 클래스 구현
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        # 가중치 초기화
        self.w1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.random.randn(hidden_size)
        self.w2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.random.randn(output_size)
    
    def forward(self, x):
        # 순전파 계산
        h = np.dot(x, self.w1) + self.b1
        h = sigmoid(h)
        y = np.dot(h, self.w2) + self.b2
        return y
    
# 입력, 은닉, 출력 노드 개수 설정
input_size = 10
hidden_size = 20
output_size = 5

# MLP 인스턴스 생성
mlp = MLP(input_size, hidden_size, output_size)

# 입력 데이터 생성
x = np.random.randn(input_size)

# 예측 결과 출력
y = mlp.forward(x)
print(y)

# 위 코드는 numpy를 이용하여 다층 퍼셉트론(MLP)을 구현
# MLP는 입력층, 은닉층, 출력층으로 구성되며, 각 층의 노드들은 서로 연결됨
# 시그모이드 함수를 활성화 함수로 사용
# MLP는 입력 데이터를 받아 순전파(forward)를 수행하여 예측 결과를 출력
