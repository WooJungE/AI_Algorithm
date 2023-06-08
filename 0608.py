#가중치 그래프 G=(V, E)가 주어졌습니다. G의 모든 신장 트리 중에서 간선들의 가중치 합이 최소인 신장 트리를 찾아보기 
#이러한 트리를 최소비용 신장 트리(MST: minimum spanning tree) 라고 함
#하나의 정점에서 시작하여 탐욕적으로 다음 정점을 선택하여 트리를 단계적으로 확장하는 방법을 사용하는 prim의 알고리즘을 이용해 최소비용 신장 트리를 구해 보기

INF = 9999

def getMinVertex(dist, selected) :
    minv = -1	
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[0] = 0
    selected = [False] * vsize

    for i in range(vsize):
        u=getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=':')
        print(dist)

        for v in range(vsize):
            if (adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

vertex = input().split()
n = int(input())
weight = [[None]*len(vertex) for i in range(len(vertex))]

for _ in range(n):
    name, node, value = input().split()
    weight[vertex.index(name)][vertex.index(node)] = int(value)
    weight[vertex.index(node)][vertex.index(name)] = int(value)

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
