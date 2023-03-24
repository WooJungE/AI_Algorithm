#자연수 n이 주어졌을 때, n²을 구해보기
#단, 복잡도가 O(n) 이 되게 만들어 보기

##compute_square_B(n) 함수로 다음과 같이 n의 제곱 값이 출력되는 함수를 작성해 보기
##이때, for 문을 사용하여 복잡도가 O(n) 이 되게 작성해 보기


def compute_square_B(n):
    sum = 0
    for i in range(n) :
        sum = sum +n
    return sum
    
n = int(input())

print(compute_square_B(n))
