#자연수 n의 팩토리얼을 계산하기
#순환 관계식을 이용하여 순환적인 팩토리얼 알고리즘을 구현해 보기

## 팩토리얼의 순환 관계식(recurrence relation)의 정의에 따라 n! 을 구하는 순환적인 팩토리얼 함수 factorial(n)을 완성하기
##이때, 순환 관계식의 초기 조건에 주의하며 코드를 작성하기


def factorial(n):
    if n == 0 :
        return 1
    else :
        return n * factorial(n-1)

n = int(input())

print(factorial(n))
