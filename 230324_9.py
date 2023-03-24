#세 개의 막대 A, B, C가 있고, 막대 A에 크기가 모두 다른 n개의 원판이 큰 것부터 아래에 놓이도록 순서대로 쌓여 있음
#이 원판들을 모두 막대 C로 옮기기
#단, 원판은 한 번에 한 개씩만 옮길 수 있고, 작은 원판 위에 큰 원판을 절대 놓을 수 없음
#모든 원판의 크기는 서로 다르고, 원판의 이동 횟수는 최소로 해야 함

##원판의 이동을 출력하는 함수 hanoi_tower(n, fr, tmp, to)를 완성해 보기
##이때, n은 이동할 원판의 개수, fr는 시작 막대, tmp은 임시 막대, to는 목표 막대임


n = int(input())

def hanoi_tower(n, fr, tmp, to):
    if(n == 1):
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)

hanoi_tower(n, 'A', 'B', 'C')
