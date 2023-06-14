#LCS의 길이뿐 아니라 두 문자열의 LCS 자체를 구하기 
#동적 계획법으로 최장 공통 부분순서를 구하는 알고리즘에서 구한 테이블을 이용해 최장 공통부분 시퀀스(LCS) 자체를 구할 수 있음
#최종 해가 저장된 셀(표의 우측 하단)을 시작으로 왼쪽 상단 모서리로 올라가면서 LCS 요소들을 추적하는 방법을 사용하여 LCS에 속한 문자들을 추출해 보기

# 동적 계획법으로 최장 공통 부분순서를 구하는 함수
def lcs_dp(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :
                L[i][j] = 0	
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    # 함수 lcs_dp_traceback(X, Y, L)를 호출
    print("LCS = ", lcs_dp_traceback(X, Y, L))
    return L[m][n] 

def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j>0:
        v = L[i][j]
        if v > L[i][j-1] and v > L[i-1][j] and v > L[i-1][j-1]:
            i -= 1
            j -=1
            lcs = X[i] + lcs
        elif v == L[i][j-1] and v > L[i-1][j]: j -= 1
        else : i -= 1
    return lcs

X = input()
Y = input()

print("X = ", X)
print("Y = ", Y)
lcs_dp(X, Y)
