#퀵 정렬(quick sort)은 평균적으로 매우 빠른 수행 속도를 자랑하는 알고리즘으로 분할 정복 전략을 사용
#퀵 정렬은 항목의 값(피벗)에 따라 분할하는 전략을 가짐
#이러한 퀵 정렬을 구현해 보기(순환 구조를 이용하면 매우 간략하게 나타낼 수 있음)

def quick_sort(A, left, right) :
    if left < right :
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] < pivot : low += 1
        while high >= left and A[high] > pivot : high -= 1
        if low < high :
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high

data = [int(n) for n in input().split()]

print("Original  : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
