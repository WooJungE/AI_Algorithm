#두 데이터가 주어졌을 때, 이들 사이의 부분순서 중에서 가장 긴 부분순서의 길이를 구해 보기
#이때 부분순서(subsequence)란 어떤 시퀀스의 일부분으로 상대적인 순서를 유지하는 시퀀스를 의미
#예를 들어, "abcdef"의 부분순서는 "abc", "acf", "df", "bcdf"등 다양함

#LCS 길이의 순환 관계식을 참고하여 순환 구조로 최장 공통 부분순서를 구하는 함수를 완성해 보기

def lcs_recur(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1+ lcs_recur(X,Y,m-1,n-1)
    else:
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n))

X = input()
Y = input()

print("X = ", X)
print("Y = ", Y)
print("LCS(분할 정복)", lcs_recur(X , Y, len(X), len(Y)))
