#완전 탐색적으로 그래프의 모든 정점을 방문하는 방법 중 깊이 우선 탐색(depth first search, DFS) 알고리즘을 구현

def dfs(graph, start, visited ):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

mygraph = dict()
n = int(input())
for i in range(n) :
    e1, e2 = input().split()[:2]
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}

print('DFS : ', end='')
dfs(mygraph, "A", set() )
print()
