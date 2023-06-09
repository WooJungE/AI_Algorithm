#각각 무게가 wtᵢ이고 가치가 valᵢ인 n개의 물건들이 있고, 이것을 배낭에 넣기
#이때, 배낭에 넣을 수 있는 용량(최대 무게)은 W를 초과하지 않아야 하고, 물건들은 잘라서 일부분만 넣을 수는 없음
#물건들의 가치의 합이 최대가 되도록 배낭을 채우고, 이때 배낭의 최대 가치를 구해 보기

#n개의 물건을 용량이 W인 배낭에 넣을 때의 최대 가치를 동적 계획법을 적용하여 구해 보기

def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][W]

n = int(input())
val = [int(n) for n in input().split()]
wt = [int(n) for n in input().split()]
W = int(input())

print("최대 가치:", knapSack_dp(W, wt, val, n)) 
