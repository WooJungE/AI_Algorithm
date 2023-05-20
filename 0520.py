#피보나치 수열(반복 구조)
#첫 번째 달에 한 쌍의 새끼 토끼를 가져옴
#토끼는 한 달이 지나면 어른으로 성장하고, 어른 토끼는 매달 새끼 토끼를 한 쌍씩 낳음
#n번째 달에는 몇 쌍의 토끼가 있을지 구해 보기. 단, 태어난 토끼는 죽지 않는다고 가정
#반복 구조의 피보나치 수열 알고리즘으로 해결해 보기

def fib_iter(n) :
    # for문을 이용해보세요!
    if (n < 2) : return n
    last = 0
    current = 1
    for i in range(2, n+1) :
        tmp = current
        current += last
        last = tmp
    return current

n = int(input())

print(fib_iter(n))
