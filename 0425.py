#리스트에서 k번째로 작은 항목을 찾아보기. 단, 리스트는 정렬되어 있지 않다.
#정렬 문제로 변환

def kth_smallest_sort(A, k): 
    A.sort()
    return A[k-1]

array = [int(n) for n in input().split()]
k = int(input())

print("입력 리스트 =", array) 
print("[정렬기법] %d번째 작은 수: " %(k), kth_smallest_sort(array, k)) 
