#피보나치 수열(분할 정복)
#첫 번째 달에 한 쌍의 새끼 토끼를 가져옴. 토끼는 한 달이 지나면 어른으로 성장하고, 어른 토끼는 매달 새끼 토끼를 한 쌍씩 낳음 
#n번째 달에는 몇 쌍의 토끼가 있을지 구해 보기. 단, 태어난 토끼는 죽지 않는다고 가정
#순환구조의 피보나치 수열 알고리즘으로 해결해 보기

def fib(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)

n = int(input())

print(fib(n))
