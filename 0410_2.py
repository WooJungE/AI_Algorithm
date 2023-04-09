#2차원 평면상에 n개의 점이 있다. 가장 인접한 쌍의 거리를 구하기.
#두 점 사이의 거리를 계산할 때는 유클리드 거리(Euclidean distance)를 이용
#유클리드 거리를 구할 때 math 모듈의 sqrt()와 거듭제곱 연산자 사용

import math
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist: 
                mindist = dist
    return mindist

n = int(input())
p = [tuple(int(m) for m in input().split()[:2]) for _ in range(n)]

print("최근접 거리:", closest_pair(p))
