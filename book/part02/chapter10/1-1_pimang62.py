'''
[기본적인 서로소 집합 알고리즘]
'''

# 노드 개수, 간선 개수 입력
v, e = map(int, input().split())    # 6 4
# 부모 테이블 초기화
parent = [0] * (v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # x번째가 부모 노드가 아니라면 계속 찾기
    if parent[x] != x:  # 4 -> 1
        return find_parent(parent, parent[x])   # 1 -> 1
    return parent[x]    # 곧바로 1! -> ## x일 때보다 효율적

# union 연산 수행
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# union 연산 각각 수행
for i in range(e):  # 4
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')
print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end = '')
for i in range(1, v+1):
    print(parent[i], end = ' ')
