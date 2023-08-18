'''
[트리 순회]
- 전위 순회(preorder) : 루트 왼쪽 오른쪽
- 중위 순회(inorder) : 왼쪽 루트 오른쪽
- 후위 순회(postorder) : 왼쪽 오른쪽 루트

입력)
n = int(input())
for _ in range(n):
    n, l, r = map(str, input().split())

'''
class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

# preorder 전위 순회
def preorder(node):
    print(node.root, end='')
    if node.left != None:
        preorder(tree[node.left])
    if node.right != None:
        preorder(tree[node.right])
    
# inorder 중위 순휘
def inorder(node):
    if node.left != None:
        inorder(tree[node.left])
    print(node.root, end='')
    if node.right != None:
        inorder(tree[node.right])

# postorder 후위 순회
def postorder(node):
    if node.left != None:
        postorder(tree[node.left])
    if node.right != None:
        postorder(tree[node.right])
    print(node.root, end='')

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = map(str, input().split())
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[root] = Node(root, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()