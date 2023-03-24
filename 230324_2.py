#자연수 n이 주어졌을 때, n²을 구해보기
#단, 복잡도가 O(1) 이 되게 만들어 보기

##compute_square_A(n) 함수로 다음과 같이 n의 제곱 값이 출력되는 함수를 작성해 보기
##이때, 복잡도가 O(1) 이 되게 작성해 보기


def compute_square_A(n):
    return n*n
   
n = int(input())

print(compute_square_A(n))
