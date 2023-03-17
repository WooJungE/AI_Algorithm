#n개의 숫자가 들어있는 배열(또는 리스트) A에서 최댓값 찾기

def find_max( A ): 
    max = A[0]
    for i in range(len(A)):
        if A[i] > max :
            max = A[i]
    return max

array = list(map(int, input().split()))

print(array, "최댓값=", find_max(array))
