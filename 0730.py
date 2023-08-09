#일 배정 문제는 n 가지의 일을 n명의 근로자에게 각각 하나씩 배정하는 문제로, 전체 배정을 최소화하는 배정을 찾는 최적화 문제
#이 문제도 분기 한정 전략을 적용해 효율적으로 해결할 수 있음
#일 배정 문제에서 어느 노드의 한계(한계 가치)는 그 노드의 서브 트리를 탐색했을 때 기대할 수 있는 가장 작은 비용, 즉 비용의 하한값이 되어야 함에 유의하기

import heapq

def job_assign_BFBnB(mat):
    N=len(mat)
    Q=[]
    bound = calcBound(mat,[])
    heapq.heappush(Q, (bound+0, (0,bound,[])))
    while len(Q) > 0 :
        total, (cost, bound, jobs) = heapq.heappop(Q)
        print("현재 노드: ", total, jobs)
        level = len(jobs)
        if level == N:
            return (total, jobs)
        for j in range(N) :
            if j not in jobs :
                jbs = jobs + [j]
                cst = cost + mat[level][j]
                bnd = calcBound(mat, jbs)
                heapq.heappush(Q,(cst+bnd, (cst, bnd, jbs)))

def calcBound(mat, jobs):
    N = len(mat)
    J = len(jobs)
    bound = 0
    for i in range(J,N):
        min = 9999
        for j in range(N):
            if j not in jobs :
                if min > mat[i][j]:
                    min = mat[i][j]
        bound += min
    return bound

Man2Job = []
n = int(input())
for i in range(n):
    Man2Job.append(list(map(int, input().split())))

total, jobs = job_assign_BFBnB(Man2Job)
print("배정 결과: ", jobs)
print("전체 비용: ", total)
