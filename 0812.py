#총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하기

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))
