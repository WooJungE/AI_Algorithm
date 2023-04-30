#리스트에 n개의 항목이 들어있음 
#리스트에서 “탐색키”를 가진 항목을 찾아보기
#단, 리스트의 항목들은 정렬되어 있음
#이진 탐색(binary search) 알고리즘을 적용해 보기
#이때 반복 구조로 이진탐 색 알고리즘을 구현해 보기

def binary_search_iter(A, key, low, high) :
    while (low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif (key > A[mid]):
            low = mid + 1
        else:
            high = mid -1
    return -1

listA = [int(n) for n in input().split()]
key = int(input())

print("입력 리스트 =", listA)
print("%d 탐색(반복) -->" %(key), binary_search_iter(listA, key, 0, len(listA)-1) )
