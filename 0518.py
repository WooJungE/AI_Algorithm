#이진 트리가 주어졌을 때, 이 트리를 후위 순회(postorder traversal) 하는 알고리즘을 구현해 보기
#루트를 방문하는 작업을 V, 왼쪽과 오른쪽 서브 트리를 방문하는 작업을 각각 L과 R

# 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')

n = int(input())
binary_tree = [TNode(0, 0, 0) for _ in range(n)]
for i in range(n) :
    data, left, right = [int(m) for m in input().split()][:3]
    binary_tree[i].data = data
    binary_tree[i].left = binary_tree[left-1] if left > 0 else None
    binary_tree[i].right = binary_tree[right-1] if right > 0 else None

root = binary_tree[0]
print('Post-Order : ', end='')
postorder(root)
print()
