#리스트에 n개의 항목이 들어 있다
#이들을 키(key)의 순서에 따라 오름차순(non-decreasing order)으로 재배치하기
#항목 자체가 키값 
#리스트에 숫자가 들어 있고, 이 리스트를 오름차순으로 정렬

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1);

def printStep(arr, val):
    print("  Step %2d = " %val, end='')
    print(arr)

A = [int(n) for n in input().split()]

print("Original  :", A)
selection_sort(A)
print("Selection :", A)
