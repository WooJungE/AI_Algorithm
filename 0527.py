#선형조사법(linear probing)에 의한 오버플로 처리를 하는 삽입 연산을 수행하는 함수 lp_insert(key)를 완성해 보기

M = 13					# 테이블의 크기
table = [None]*M			# 테이블 만들기: None으로 초기화
def hashFn(key) :		# 해시 함수
    return key % M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None) :
        id = (id + 1 +M) % M
        count -= 1
    if count > 0 :
        table[id] = key
    return

n = int(input())
for _ in range(n):
    lp_insert(int(input()))

print(table)
