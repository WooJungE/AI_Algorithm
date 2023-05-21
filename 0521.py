#피보나치 수열(축소 정복 기법의 행렬 거듭제곱 이용)
#첫 번째 달에 한 쌍의 새끼 토끼를 가지고 옴
#토끼는 한 달이 지나면 어른으로 성장하고, 어른 토끼는 매달 새끼 토끼를 한 쌍씩 낳음
#n번째 달에는 몇 쌍의 토끼가 있을지 구해 보기. 단, 태어난 토끼는 죽지 않는다고 가정
#축소 정복 기법의 행렬 거듭제곱 알고리즘을 이용해 해결해 보기

def fib_mat(n) :
    if n < 2 :
        return n
    mat = [[1,1], [1,0]]
    result = powerMat(mat, n)
    return result[0][1]

# powerMat(x, n) 함수
def powerMat(x, n) :
	if n == 1 :
		return x
	elif (n % 2) == 0 :
		return powerMat(multMat(x,x), n // 2)
	else :
		return multMat(x, powerMat(multMat(x,x), (n - 1) // 2)) 

# multMat(M1, M2) 함수
def multMat(M1, M2):
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result

n = int(input())

print(fib_mat(n))
