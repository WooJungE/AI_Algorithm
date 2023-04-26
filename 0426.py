#리스트에서 k번째로 작은 항목을 찾아보기. 단, 리스트는 정렬되어 있지 않다. 이를 축소 정복 기법을 적용하여 풀기

def quick_select(A, left, right, k): 
    pos = partition(A, left, right)
    if (pos+1 == left+k):
        return A[pos]
    elif (pos+1 > left+k) :
        return quick_select(A, left, pos-1, k)
    else :
        return quick_select(A, pos+1, right, k-(pos+1-left))

def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high) :
        while low <= right and A[low] <pivot : low +=1
        while high >= left and A[high] > pivot : high -=1
        if low < high :
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high

array = [int(n) for n in input().split()]
k = int(input())

n = len(array)
print("입력 리스트 =", array) 
print("[축소정복] %d번째 작은 수: " %(k), quick_select(array, 0, n-1, k)) 
