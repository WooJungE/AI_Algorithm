#0분기 한정 기법을 이용한 0-1 배낭 채우기 문제에서 한계 합 계산 방법을 개선해 보기
#개선된 한계 가치는 더 작은 값이 되어야 함
#이것은 어떤 노드의 서브 트리에서 기대되는 값을 좀 더 빡빡하게 계산하는 것으로, 그 노드의 기대 가치가 줄면 지금까지의 최대가치에 의해 가지치기 될 가능성이 더 커지고, 탐색의 효율이 높아짐
#남은 물건들을 분할 가능한 배낭 문제로 생각하고, 무게당 가격이 높은 물건부터 배낭의 용량을 꽉 채워서 넣고, 이때의 가치 합을 한계 가치로 사용하는 전략 이용하기

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
        newBound  = bound2(obj, W, level, newWeight, newProfit)
	    
        if newBound >= maxProfit :
            knapsack.append(obj[level][2])
            maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight, 
									newProfit, maxProfit, newBound)  
            knapsack.pop()
    newWeight = weight
    newProfit = profit
    newBound  = bound2(obj, W, level, newWeight, newProfit)
	
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight,
									 newProfit, maxProfit, newBound) 
    return maxProfit
	
def bound2(arr, W, level, weight, profit) :
    if weight>W:
       return 0
    pBound = profit
    tWeight = weight
    j = level + 1
    n = len(arr)
	
    while j < n and (tWeight+obj[j][0] <= W):
        tWeight += arr[j][0]
        pBound += arr[j][1]
        j+=1
	    
    if(j<n) :
        pBound +=(W-tWeight) * (arr[j][1]/arr[j][0])
    return pBound
	
obj = []
n = int(input())

for i in range(n):
    w, p, name = input().split()
    obj.append((float(w), float(p), name))

W = float(input())
obj.sort(key= lambda e : e[1]/e[0], reverse=True)

print(obj)
print("0-1배낭문제(분기 한정): ", knapSack_bnb(obj, [], W, 0,0,0,0, 0) )
