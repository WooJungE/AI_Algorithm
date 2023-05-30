#선형조사법(linear probing)에 의한 오버플로 처리를 하는 삭제 연산을 수행하는 함수 lp_delete(key)를 완성해 보기

# 테이블의 크기
M = 13	

# 해시 함수
def hashFn(key) :		
    return key % M

def lp_delete(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None :return
        if table[id] != -1 and table[id] == key :
            table[id] = -1
            return
        id = (id+1+M) % M
        count -= 1

table = [None if m == "None" else int(m) for m in input().split()]
key = int(input())

lp_delete(key)
print(table)
