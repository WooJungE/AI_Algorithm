#선형조사법(linear probing)에 의한 오버플로 처리를 하는 탐색 연산을 수행하는 함수 lp_search(key)를 완성해 보기

M = 13					# 테이블의 크기
def hashFn(key) :		# 해시 함수
    return key % M

def lp_search(key) :
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None :
            return None
        if table[id] == key :
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

table = [None if m == "None" else int(m) for m in input().split()]
key = int(input())

print(lp_search(key))
