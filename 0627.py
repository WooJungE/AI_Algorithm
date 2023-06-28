#양수로 이루어진 집합 S와 어떤 수 M이 주어짐
#이 S의 부분집합 중에 원소의 합이 M이 되는 모든 가능한 부분 집합을 찾아보기
#순환 호출을 이용해 백트래킹 알고리즘을 구성하여 해결할 수 있음
#이때 조금 더 많은 가지치기를 위해 다음과 같은 추가적인 백트래킹 조건을 사용해 보기
#remaining을 현재 해에 선택되지 않고 남은 집합 S의 모든 숫자의 합
#remaining과 현재 해의 합이 M보다 작으면 남은 숫자를 모두 해에 넣어도 M을 절대 만들 수 없음 
#백트래킹 하기

def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S, M, 0, [], sum(S))

def DFS_sum_of_subsets(S, M, level, sol, remaining):
    if sum(sol) == M:
        print(sol)
        return
    if sum(sol)>M :
        return
    for i in range(level, len(S)):
        sol.append(S[i])
        DFS_sum_of_subsets(S, M, i+1, sol, remaining-S[i])
        sol.pop()

nums = list(map(int, input().split()))
M = int(input())

solution = all_sum_of_subsets(nums, M)
print("입력 집합 :", nums, "M=", M )
