#길이가 n인 입력 문자열 T와 길이가 m인 패턴 문자열 P가 있음
#항상 n >= m이라고 가정
#모든 문자열은 알파벳과 띄어쓰기만으로 구성되어 있다고 가정
#대문자와 소문자를 구분(예를 들어, ‘a’와 ‘A’를 다른 문자)
#T에서 가장 먼저 나타나는 P의 위치를 찾기
#패턴이 없으면 -1을 반환합니다.

def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j=0
        while j < m and P[j] == T[i+j] :
            j = j+1
        if j == m:
            return i
    return -1

T = input()
P = input()

print(string_matching(T, P))
