#부분 문제의 해를 메모리에 저장한다는 점은 메모이제이션과 같지만, 메모리의 항목들을 순서에 따라 상향식으로 채워나가는 것에 초점을 맞추는 테이블화(tabulation)를 이용하여 피보나치 수열 알고리즘을 구현해 보기

def fib_dp_tab(n) :
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]	

n = int(input())

print('Fibonacci(%d) = '%n, fib_dp_tab(n))
