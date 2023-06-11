#두 데이터가 주어졌을 때, 이들 사이의 부분순서 중에서 가장 긴 부분순서의 길이를 구해 보기
#이때 부분순서(subsequence)란 어떤 시퀀스의 일부분으로 상대적인 순서를 유지하는 시퀀스를 의미
#예를 들어, "abcdef"의 부분순서는 "abc", "acf", "df", "bcdf"등 다양함
#동적 계획법으로 최장 공통 부분순서를 구하는 함수를 완성해 보기

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
    return L[m][n]

X = input()
Y = input()

print("X = ", X)
print("Y = ", Y)
print("LCS(동적 계획)", lcs_dp(X , Y) )
