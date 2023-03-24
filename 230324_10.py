#자연수 n을 이진수로 표시하였을 때 총 비트 수를 return 하는 함수 binary_digits(n)를 완성하기 
#순환 구조로 알고리즘을 작성

def binary_digits(n):
    if n <= 1 :
        return 1
    else :
        return 1+binary_digits(n//2)

n = int(input())

print(binary_digits(n))
