#정렬 문제를 축소 정복 기법으로 해결한 삽입 정렬 알고리즘을 구현
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
        printStep(A, i)

def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)

data = [int(x) for x in input().split()]

print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)
