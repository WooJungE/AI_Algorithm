#해시 함수에서 탐색키가 문자열인 경우, 보통 각 문자에 정수를 대응 시켜 바꾸게 됨
#각 문자의 아스키코드나 유니코드 값을 그대로 이용할 수 있음. 가능하면 문자열 안의 모든 문자를 골고루 사용하는 것이 좋음.
#문자열 key를 받아 각 문자의 코드 값을 모두 더하고 이를 테이블 크기 M으로 나머지 연산하여 주소를 계산하는 해시함수를 완성해 보기

M = 13              # 테이블의 크기
table = [None]*M    # 테이블 만들기: None으로 초기화

def hashFn(key) :
    sum = 0
    for c in key :
        sum = sum + ord(c)
    return sum % M

# 선형 조사법의 삽입 알고리즘
def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
    # while count>0 and (table[id] != None) :
        id = (id + 1 + M) % M
        count -= 1
    if count > 0 :
        table[id] = key	
    return

n = int(input())
for _ in range(n) :
    lp_insert(input())

print(table)
