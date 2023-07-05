#N-Queen 문제는 NxN의 체스보드에 N개의 퀸을 놓는 문제
#이때, 어떤 퀸도 다른 퀸을 공격할 수 없어야 함.
#퀸은 수평이나 수직, 또는 대각선 위치에 있는 적을 공격할 수 있음.
#결국 모든 퀸이 가로와 세로, 대각선 방향으로 다른 퀸과 중복되어 놓이지 않도록 퀸들을 배치하는 것이 핵심
#이때, 백트래킹 전략을 이용하여 N-Queen 문제를 해결해 보기

def isSafe(board, x, y):
    N = len(board)
    for i in range(y):
        if board[i][x] == 1: return False
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] == 1: return False
    return True

def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        printBoard(board)
        return
    for x in range(N):
        if isSafe(board, x, y):
            board[y][x]=1
            solve_N_Queen(board, y+1)
            board[y][x] = 0

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

N = int(input())

board = [[0 for i in range(N)] for j in range(N)]
solve_N_Queen(board, 0)
