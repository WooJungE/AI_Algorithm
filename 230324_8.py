#자연수 n의 팩토리얼을 계산해보기
#이때, 반복 구조의 팩토리얼 알고리즘을 구현해 보기

##순환적인 팩토리얼 알고리즘을 반복 구조로 변환한 팩토리얼 함수 factorial(n)을 완성해 보기


def factorial(n):
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result

n = int(input())

print(factorial(n))
