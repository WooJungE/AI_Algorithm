#두 문자열 S와 T가 주어졌고 S를 편집하여 T로 변환시키려고 함
#사용할 수 있는 편집 연산은 한 문자의 삽입(insertion)이나 삭제(deletion), 그리고 대체(substitution) 연산 뿐
#S를 T로 변환시키는데 필요한 최소 편집 연산의 회수(편집거리)를 구해 보기

#이때, 동적 계획법, 메모이제이션을 사용하여 편집거리를 구해 보기


def edit_distance_mem(S, T, m, n, mem): 
    if m == 0: return n
    if n ==0 : return m

    if mem[m-1][n-1] == None :
        if S[m-1] == T[n-1]:
            mem[m-1][n-1] = edit_distance_mem(S, T, m-1, n-1, mem)
        else:
            mem[m-1][n-1] = 1+ \
            min( edit_distance_mem(S, T, m, n-1, mem),
            edit_distance_mem(S, T, m-1, n, mem),
            edit_distance_mem(S, T, m-1, n-1, mem))
    return mem[m-1][n-1]

S = input()
T = input()

m = len(S)
n = len(T)
print("문자열:", S, T)
mem = [[None for _ in range(n)] for _ in range(m)] 
dist = edit_distance_mem(S, T, m, n, mem)
print("편집거리(메모이제이션)=", edit_distance_mem(S, T, m, n, mem))
