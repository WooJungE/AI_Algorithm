#카운팅 정렬 알고리즘을 구현한 함수 counting_sort(A)를 완성해 보기

def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL

    for i in A:
        count[i] += 1
    
    for i in range(1, MAX_VAL) :
        count[i] += count[i-1]

    for i in range(len(A)):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)) :
        A[i] = output[i]

data = [int(n) for n in input().split()]

MAX_VAL = 10
print("Original  : ", data)
counting_sort(data)             # 카운팅 정렬
print("Counting  : ", data)
