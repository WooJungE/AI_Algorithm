#무방향 가중치 그래프가 주어졌을 때 그래프의 모든 정점 사이의 최단 경로의 길이를 구해 보기
#이때, 경로의 길이는 그 경로에 포함된 간선들의 가중치 합이고, 간선의 가중치로 음수는 허용하지 않음

#모든 정점 간의 최단 경로 거리 계산 문제에 대한 알고리즘인 Floyd-Warshall알고리즘(줄여서 Floyd 알고리즘) 은 동적 계획법을 이용해 모든 정점에서 다른 모든 정점까지의 최단 경로를 한꺼번에 구하는 방법

#Floyd 알고리즘을 적용하여 무방향 가중치 그래프의 최단 경로를 구하는 함수를 완성해 보기

import copy	
def shortest_path_floyd(vsize, W):
    D=[[]]
    D = copy.deepcopy(W)
    # 정점 k를 추가할 때마다 반드시 printD(D)를 호출
    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                if (D[i][k]+D[k][j]<D[i][j]) : 
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)

# 현재의 최단거리 행렬 D를 화면에 출력하는 함수
def printD(D):
    vsize = len(D)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (D[i][j] == INF) : print(" INF ", end='')
            else : print("%4d "%D[i][j], end='')
        print("")

INF = 9999
vsize = int(input())
n=int(input())
weight = [[INF] * vsize for _ in range(vsize)]

for i in range(vsize):
    weight[i][i] = 0

for _ in range(n):
    i, j, w = [int(m) for m in input().split()[:3]]
    weight[i][j] = w
    weight[j][i] = w

print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vsize, weight)
