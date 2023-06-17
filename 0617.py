#두 문자열 S와 T가 주어졌고 S를 편집하여 T로 변환시키려고 함
#사용할 수 있는 편집 연산은 한 문자의 삽입(insertion)이나 삭제(deletion), 그리고 대체(substitution) 연산 뿐
#S를 T로 변환시키는데 필요한 최소 편집 연산의 회수(편집거리)를 구해 보기
#이때, 분할 정복법을 이용하여 순환 구조로 편집 거리 구하기

def edit_distance(S, T, m, n):
    if m == 0: return n
    if n == 0: return m 

    if S[m-1] == T[n-1]:
        return edit_distance(S, T, m-1, n-1)

    return 1+min(edit_distance(S,T,m, n-1),
    edit_distance(S, T, m-1, n),
    edit_distance(S, T, m-1, n-1))

S = input()
T = input()

m = len(S)
n = len(T)
print("문자열:", S, T)
print("편집거리(분할정복)=", edit_distance(S, T, m, n))
