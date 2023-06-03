#한 번 계산한 값을 저장해 두었다가 재활용하는 최적화 기법인 메모이제이션(memoization) 을 이용하여 피보나치 수열 알고리즘을 구현해 보기

def fib_dp_mem(n) :
    if(mem[n]==None) :
        if n < 2 :
            mem[n] = n
        else :
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

n = int(input())

mem = [None] * (n+1)
