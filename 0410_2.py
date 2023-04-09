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
