#0-1 배낭 채우기 문제는 무게와 가치가 주어진 n개의 물건이 있을 때, 배낭에 담을 수 있는 최대 무게(용량) W를 초과하지 않으면서 물건들의 가치의 합이 최대가 되도록 만들어야 하는 문제
#어떤 노드의 무게 합이 이미 배낭 용량을 초과했다면 서브 트리를 더 탐색할 필요가 없다는 아이디어를 이용하여 백트래킹 전략으로 이 문제를 해결할 수 있음
#이때, 분기 한정(branch and bound)을 이용하면 백트래킹의 효율을 추가로 향상할 수 있음
#분기 한정은 N의 서브 트리에서 기대할 수 있는 최대 가치를 먼저 계산하기
#만약 최대 기대 가치가 10이라고 하면, N의 서브 트리에서는 N까지 확정된 가치 60과 최대 기대 가치 10을 합한 70 이상의 해가 나올 수 없음
#현재 알고 있는 최대 가치가 80이라고 할 때 이 서브 트리를 탐색할 필요가 없으므로 바로 백트래킹
#분기 한정을 위해서는 상태 공간 트리의 각 노드를 탐색할 때마다 지금까지 알고 있는 최적해인 최고가치(maximum profit) 과 현재 노드 N에서 기대할 수 있는 최선의 가치합인 한계 가치(bounded profit) 을 계산해야 함에 유의하며 분기 한정 기법을 이용해 0-1 배낭 채우기 문제를 해결해 보기

# 노드를 탐색하는 순서와 각 노드에서 계산된 값들을 출력하는 함수
def printNode(knapsack, level, weight, profit, bound, maxProfit):
    print("%d %-16s :  %3.1fKg 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)"%
          (level, knapsack, weight, profit, bound, maxProfit))
  
def knapSack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound) : 
    printNode(knapsack, level, weight, profit, bound, maxProfit)
  
    if (level == len(obj)) :
        return maxProfit
      
    if weight + obj[level][0] <= W :
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
      
        if newProfit > maxProfit :
            maxProfit = newProfit
        newBound  = bound1(obj, W, level, newWeight, newProfit)
      
        if newBound >= maxProfit :
            knapsack.append(obj[level][2])
            maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight, 
                           newProfit, maxProfit, newBound)  
            knapsack.pop()
    newWeight = weight
    newProfit = profit
    newBound  = bound1(obj, W, level, newWeight, newProfit)
  
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight,
                            newProfit, maxProfit, newBound) 
    return maxProfit
  
def bound1(obj, W, level, weight, profit) :
    if weight > W:
        return 0
    pBound = profit
  
    for j in range(level+1, len(obj)):
        pBound += obj[j][1]
    return pBound 
n = int(input())
obj = []

for _ in range(n):
    weight, value, name = input().split()
    obj.append((float(weight), float(value), name))
  
W = int(input())

print(obj)
print("0-1배낭문제(분기 한정): ")
knapSack_bnb(obj, [], W, 0,0,0,0, 0) 
