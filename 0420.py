#리스트에 n개의 항목이 들어있음
#이 리스트에서 “탐색키”를 가진 항목을 찾아보기
#단, 리스트의 항목들은 정렬되어 있음
#이진 탐색(binary search) 알고리즘을 적용해 보기
#이때 순환구조로 이진 탐색 알고리즘을 구현

def binary_search(A, key, low, high) :
    if (low <= high) :
        mid = (low + high) //2
        if key == A[mid] :
            return mid
        elif key < A[mid] :
            return binary_search(A, key, low, mid-1)
        else :
            return binary_search(A, key, mid+1, high)
    return -1

listA = [int(n) for n in input().split()]
key = int(input())

print("입력 리스트 =", listA)
print("%d 탐색(순환) -->" %(key), binary_search(listA, key, 0, len(listA)-1) )
