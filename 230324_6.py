#자연수 n을 이진수로 표시하였을 때 총 비트 수를 구해보기
#이때, 반복 구조로 총 비트 수를 구하는 알고리즘을 작성해 보기

##자연수 n을 이진수로 표시하였을 때 총 비트 수를 return 하는 함수 binary_digits(n)를 완성해 보기
##이때, 반복 구조로 알고리즘을 작성해보기


def binary_digits(n):
    count = 1
    while n > 1 :
        count = count + 1
        n = n // 2
    return count

n = int(input())

print(binary_digits(n))
