#동적 계획법을 이용해 이항계수 C(n, k)를 계산하는 함수를 완성해 보기

def bino_coef_dp(n, k):
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j in range(min(i,k)+1):
                if j == 0 or j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1] + C[i-1][j] 
    return C[i][j]

n = int(input())
k = int(input())

print("C(%d,%d) =" %(n, k), bino_coef_dp(n, k))
