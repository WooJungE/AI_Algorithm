#n개의 항목으로 이루어진 어떤 리스트 A가 주어졌을 때 A에 중복된 항목이 있는지 없는지를 검사해 보기

##같은 항목이 있으면 False를, 같은 항목이 없으면 True를 반환하는 함수 unique_elements(A)를 완성해보기


A = [int(n) for n in input().split()]

def unique_elements(A):
    n = len(A)
    for i in range(n-1) :
        for j in range(i+1, n) :
            if A[i] == A[j] :
                return False
    return True

print(unique_elements(A))
