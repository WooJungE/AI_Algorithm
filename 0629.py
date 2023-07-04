#2차원 배열로 주어진 미로에서 백트래킹을 이용해 출구를 찾는 방법을 생각해 보기
#0은 벽을 나타내고, 1은 갈 수 있는 칸을, 그리고 2는 출구를 나타냄

def isSafe( maze, x, y, mark ):
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y>=0 and y<H :
        if maze[y][x]!=0 and mark[y][x]==0:
            return True
    return False 
  
# 미로맵 maze와 현재 위치 (x, y)를 받아 출구를 찾는 미로탐색 주 함수
def solve_maze( maze, x, y ):
    W, H = len(maze[0]), len(maze)                  # 미로 맵의 크기
    sol = [[0 for j in range(W)] for i in range(H)] # 해 경로 맵
    mark= [[0 for j in range(W)] for i in range(H)] # 방문 맵
      
    if DFS_maze(maze, x, y, sol, mark) == False:	# 탐색 실패
        print("출구를 찾을 수 없음") 
    else :    									# 탐색 성공
        for i in sol: print(i)					# 해 경로 맵 출력
          
def DFS_maze(maze, x, y, sol, mark):
    W, H = len(maze[0]), len(maze)
    if not isSafe(maze, x, y, mark):
        return False
    mark[y][x] = 1
    sol[y][x] = 1
    if maze[y][x] ==2:
        return True
      
    # 우-하-좌-상 순으로 탐색하는 코드
    if DFS_maze(maze, x+1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y+1, sol, mark)==True: return True
    if DFS_maze(maze, x-1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y-1, sol, mark)==True: return True
    sol[y][x] = 0
    return False

x, y = map(int, input().split())

maze = [ [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
         [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solve_maze(maze, x, y) 
