#x의 n-거듭제곱인 xⁿ을 계산해 보기
#파이썬의 ** 연산자를 사용하지 말고, 곱셈을 이용해 직접 계산하는 알고리즘을 생각해 보기
#억지 기법으로 거듭제곱을 계산해 보기

def slow_power(x, n) :
    result = 1.0
    for i in range(n):
        result = result * x
    return result

x = int(input())
n = int(input())

print("억지기법(%d**%d) =" %(x, n), slow_power(x, n))
