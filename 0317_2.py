#두 자연수 a와 b의 최대 공약수(Greatest Common Divisor)를 구하기
#유클리드 알고리즘(Euclid’s algorithm)을 이용하기
#gcd(a, b) = gcd(b, a mod b) 
#반드시 a가 b보다 작지 않아야 함

a = 0
b = 0
a = int(input())
b = int(input())

def gcd(a, b):  #a가 b보다 작지 않아야 함
    while b != 0 :  #b가 0이 아닌 동안
        r = a % b
        a = b
        b = r
    return a    #결과 반환

print("%d, %d의 최대 공약수 =" % (a, b), gcd(a, b))
