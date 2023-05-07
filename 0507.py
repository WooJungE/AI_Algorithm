#정렬 문제에 분할 정복 전략을 적용하면 매우 효율적인 알고리즘을 만들 수 있음
#대표적인 정렬 알고리즘의 하나인 병합 정렬(merge sort)을 이용하여 주어지는 리스트 A를 정렬해 보기
#순환 구조를 이용하면 매우 간략하게 나타낼 수 있음

def merge_sort(A, left, right) :
    if left < right :
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)
        
def merge(A, left, mid, right) :
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
        else :
            sorted[k] = A[j]
            j, k = j+1, k+1
    if i>mid :
            sorted[k:k+right-j+1] = A[j:right+1]
    else:
            sorted[k:k+mid-i+1]=A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]

data = [int(n) for n in input().split()]

sorted = [0] * len(data)			# 길이가 len(data)인 임시 리스트를
print("Original  : ", data)			# 만들고 모든 항목을 0으로 초기화
merge_sort(data, 0, len(data)-1)	# 병합 정렬
print("MergeSort : ", data)
