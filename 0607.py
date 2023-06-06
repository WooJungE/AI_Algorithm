#각각 무게가 wtᵢ이고 가치가 valᵢ인 n개의 물건들이 있고, 이것을 배낭에 넣으려고 함
#이때, 배낭에 넣을 수 있는 용량(최대 무게)은 W를 초과하지 않아야 하고, 물건들은 잘라서 일부분만 넣을 수는 없음
#물건들의 가치의 합이 최대가 되도록 배낭을 채우고, 이때 배낭의 최대 가치를 구해 보기
#n개의 물건을 용량이 W인 배낭에 넣을 때의 최대 가치 A(n, W)에 대한 순환 관계식을 기반으로 분할 정복 기법을 적용하여 이 문제를 해결해 보기

def knapSack_bc(W, wt, val, n): 
    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return knapSack_bc(W, wt, val, n-1)
    else:
        valWithout = knapSack_bc(W, wt, val, n-1)
        valWith = val[n-1] + knapSack_bc(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout)

n = int(input())
val = [int(n) for n in input().split()]
wt = [int(n) for n in input().split()]
W = int(input())

print("최대 가치:", knapSack_bc(W, wt, val, n)) 
