#m×m의 정방형 행렬 M의 n-거듭제곱인 Mⁿ을 계산해 보기
#축소 정복 전략으로 행렬의 거듭제곱을 구현할 수 있음
#두 행렬을 곱하는 multMat(M1, M2)함수가 이미 있다고 가정하고 행렬 거듭제곱 코드를 구현해 보기

def powerMat(x, n) :
    if n == 1 :
        return x
    elif (n%2) == 0:
        return powerMat(multMat(x, x), n//2)
    else :
        return multMat(x, powerMat(multMat(x,x), (n-1) // 2))

def multMat(M1, M2):
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result

n = int(input())
row = int(input())
x = [[int(m) for m in input().split()] for _ in range(row)]

result = powerMat(x, n)
print()
for row in result:
    for num in row:
        print(num, end=' ')
    print()
