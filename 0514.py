#이진 트리가 주어졌을 때, 이 트리의 높이를 구하는 분할 정복 전략

class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크

def calc_height(root) :
    if root is None :
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1

n = int(input())
binary_tree = [TNode(0, 0, 0) for _ in range(n)]
for i in range(n) :
    data, left, right = [int(m) for m in input().split()][:3]
    binary_tree[i].data = data
    binary_tree[i].left = binary_tree[left-1] if left > 0 else None
    binary_tree[i].right = binary_tree[right-1] if right > 0 else None

root = binary_tree[0]
print("트리의 높이 =", calc_height(root))
