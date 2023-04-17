#완전 탐색적으로 그래프의 모든 정점을 방문하는 방법 중 너비 우선 탐색(breadth first search, BFS) 알고리즘을 구현

import queue

def bfs(graph, start):
    visited = { start }
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end = ' ')
        nbr = graph[v] - visited
        for u in nbr :
            visited.add(u)
            que.put(u)

mygraph = dict()
n = int(input())
for i in range(n) :
    e1, e2 = input().split()[:2]
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}

print('BFS : ', end='')
bfs(mygraph, "A")
print()
