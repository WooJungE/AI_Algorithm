#그래프에서 인접한 노드가 같은 색을 갖지 않도록 k개의 색을 이용해 칠하는 문제를 생각해 봅시다. 백트래킹을 통해 이 문제를 효율적으로 해결해 보기
#백트래킹은 첫 번째 정점부터 시작하여 순서에 따라 한 정점씩 색칠하는 방법을 사용
#정점 v에 어떤 색 c를 칠하기 위해 먼저 v의 인접 정점을 조사
#v의 인접 정점 중 색이 c인 정점이 있으면 백트래킹하고 다른 색을 시도
#만약 v에 c를 칠했다면 다음 노드를 같은 방법을 처리
#이 과정을 그래프의 모든 노드가 색칠될 때까지 반복 
#모든 노드를 검사했는데도 해가 없으면 이 트리는 k개의 색으로는 칠할 수 없는 것

def isSafe(g, v, c, color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True

def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True

    for c in range(1, k+1):
        if isSafe(graph, v, c, color):
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0
    return False

# 그래프 색칠 주 함수
def graphColouring(graph, k, states): 
    color = [0] * len(graph)       # 정점의 색 배정 리스트: 초기 0
    ret = DFS_graph_coloring(graph, k, 0, color)  # 0번 정점부터 처리
    if ret : 
        for i in range(len(graph)) :
            print("%3s = "%states[i], color_name[color[i]])
    else :
        print("그래프를 색칠할 수 없음!")

k = int(input())

states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라", "주황"]
g = [ [0, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 0, 0, 1, 1, 0],
      [1, 1, 1, 0, 1, 1],
      [0, 0, 1, 1, 0, 1],
      [0, 0, 0, 1, 1, 0],]
print("색상 %d개:" %(k))
graphColouring(g, k, states) 
