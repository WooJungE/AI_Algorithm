#리스트에 n개의 항목이 들어 있음
#이 리스트에서 “탐색키” 를 가진 항목을 찾아보기 
#만약 찾는 항목이 있으면 그 항목의 인덱스를 반환하고, 없으면 -1을 반환
#단, 리스트의 항목들은 정렬되어 있지 않음

def sequential_search(A, key):
    for i in range(len(A)) :
        if A[i] == key :
            return i
    return -1

A = [int(n) for n in input().split()]

key = int(input())

print(sequential_search(A, key))
