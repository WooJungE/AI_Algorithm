#방향 그래프 G=(V, E) 가 주어짐
#G에 존재하는 각 정점의 선행 순서를 위배하지 않으면서 모든 정점을 순서대로 나열하기
#이때, 축소 정복 기법을 사용하여 구현

def topological_sort(graph):
    inDeg = {}
    for v in graph :
        inDeg[v]=0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    vlist = []
    for v in graph :
        if inDeg[v] == 0 :
            vlist.append(v)
    while vlist : 
        v = vlist.pop()
        print(v, end = ' ')
        for u in graph[v] :
            inDeg[u] -= 1
            if inDeg[u] == 0 :
                vlist.append(u)

mygraph = dict()
for i in range(int(input())):
    mygraph[chr(ord('A')+i)] = set()

for _ in range(int(input())):
    e1, e2=input().split()[:2]
    mygraph[e1] |= {e2}

print('topological_sort: ')
topological_sort(mygraph)
print()
