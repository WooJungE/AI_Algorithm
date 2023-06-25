#n개의 원소를 가진 집합이 주어졌을 때 모든 가능한 원소의 순서를 나열해 보기
#순환 구조로 백트래킹을 이용한 순열 생성 알고리즘을 구성해 보기
#all_permutations(data) 함수는 필요한 자료들을 초기화하고 순환 호출을 시작함
#DFS_permutation (data, sol, level, bUsed) 함수는 실제로 순환 호출을 통해 상태 공간 트리를 탐색하는 구조를 갖음

def all_permutations(data):
    bUsed = [False] * len(data)
    DFS_permutation (data, [], 0, bUsed)

def DFS_permutation (data, sol, level, bUsed):
    if level == len(data):
        print(sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            DFS_permutation (data, sol, level+1, bUsed)
            sol.pop()
            bUsed[i] = False

data = input().split()

all_permutations(data)
