#이항계수의 순환적 정의에 기반하여 분할 정복을 이용해 순환구조로 이항계수 C(n, k)를 계산하는 함수를 완성해보기

def bino_coef_dc(n, k):
    if k == 0 or k == n :
        return 1
    return bino_coef_dc(n-1, k-1) + bino_coef_dc(n-1, k)

n = int(input())
k = int(input())

print("C(%d,%d) =" %(n, k), bino_coef_dc(n, k))
