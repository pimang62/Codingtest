'''
[나무 재테크]
n by n, r행 c열 1-indexed
처음엔 양분 모든 칸에 5

m개의 나무를 구매해 땅에 심음
1 by 1에 여러 개 가능!

봄에는 자신의 나이만큼 양분 먹고 1증가
여러 개면 나이가 "어린" 나무부터 먹는다

양분이 부족하면 바로 죽음
여름에는 (죽은 나무 나이 // 2) 양분으로

가을에는 나무 번식, 나이가 5의 배수
인접한 8개의 칸에 나이가 1인 나무 생김

겨울에는 땅을 돌아다니며 양분 추가
각 칸에 추가되는 양분의 양은 A[r][c]

k년이 지난 후 살아있는 나무의 개수?

5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3 -> 4 -> 5
3 2 3 

5 5 5 5 5s
0 5 5 5 5
5 1 5 5 5
5 5 5 5 5
5 5 5 5 5

{(1, 0): [3], (2, 1): [3]}
{(1, 0): [4], (2, 1): [4]}  # 먹고 추가하기
{(1, 0): [5, 1], (2, 1): [5, 1], +4 +7 }

tree -> dead & remain -> tree
'''
from collections import deque

n, m, k = map(int, input().split())

add = [list(map(int, input().split())) for _ in range(n)]  # 추가되는 양분의 양

graph = [[5]*n for _ in range(n)]  # 5로 초기화 된 배열
tree = [[deque() for _ in range(n)] for _ in range(n)]  # 내부 queue

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n  # True or False

for _ in range(k):
    
    for i in range(n):
        for j in range(n):
            # 봄
            dead = 0  # += 죽은 나무 나이 // 2
            remain = deque()  # 새로운 배열로 교체
            while tree[i][j]:
                tmp = tree[i][j].popleft()
                if graph[i][j] < tmp:
                    dead += tmp//2
                else:  # graph[i][j] >= tmp
                    graph[i][j] -= tmp
                    remain.append(tmp+1)
            # 여름
            graph[i][j] += dead
            tree[i][j] = remain
    
    # 가을
    for i in range(n):
        for j in range(n):
            # 5의 배수인지 체크
            for is_five in tree[i][j]:
                if is_five % 5 == 0:
                    for (nx, ny) in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                        if not in_range(nx, ny):
                            continue
                        tree[nx][ny].appendleft(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += add[i][j]

answer = 0  # tree 전체 길이
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

# answer = sum(len(tree[i][j]) for i in range(n) for j in range(n))
print(answer)

"""timeout
import heapq

n, m, k = map(int, input().split())

add = [list(map(int, input().split())) for _ in range(n)]  # 추가되는 양분의 양

graph = [[5]*n for _ in range(n)]  # 5로 초기화 된 배열

tree = {}
for _ in range(m):  # (나무의 위치), 나무의 나이
    x, y, z = map(int, input().split())
    if (x-1, y-1) not in tree:
        tree[(x-1, y-1)] = [z]
    else:
        heapq.heappush(tree[(x-1, y-1)], z)

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

for _ in range(k):  # k년 반복
    new_tree = {}
    # 봄
    for (i, j), q in tree.items():
        dead = {}
        while q:
            tmp = heapq.heappop(q)
            if graph[i][j] < tmp:  # 죽은 양분 넣기
                dead[(i, j)] = dead.get((i, j), []) + [tmp//2]
            else:  # graph[i][j] >= tmp
                graph[i][j] -= tmp
                if (i, j) not in new_tree:
                    new_tree[(i, j)] = [tmp+1]
                else:
                    heapq.heappush(new_tree[(i, j)], tmp+1)
        # 여름
        for (i, j), dlist in dead.items():
            graph[i][j] += sum(dlist)
    # 가을
    update_tree = new_tree.copy()
    for (i, j), vlist in new_tree.items():
        for v in vlist:
            if v % 5 == 0:  # 5의 배수가 하나라도 있으면
                for (nx, ny) in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if not in_range(nx, ny):
                        continue
                    if (nx, ny) not in update_tree:
                        update_tree[(nx, ny)] = [1]
                    else:
                        heapq.heappush(update_tree[(nx, ny)], 1)

    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += add[i][j]
    
    tree = update_tree  # 갱신
    
print(sum(len(val) for val in tree.values()))
"""

"""timeout
# import heapq
from collections import deque

n, m, k = map(int, input().split())

add = [list(map(int, input().split())) for _ in range(n)]  # 추가되는 양분의 양

graph = [[5]*n for _ in range(n)]  # 5로 초기화 된 배열

tree = deque()  # "최소 heap" x -> queue로 변경
for _ in range(m):
    x, y, z = map(int, input().split())
    # heapq.heappush(tree, (z, x-1, y-1))
    tree.append((z, x-1, y-1))

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

# [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
dx = [-1, -1, -1, 0, 0, +1, +1, +1]  # 시간 초과 해결!
dy = [-1, 0, +1, -1, +1, -1, 0, +1]

for _ in range(k):
    dead = deque()  # deque : popleft
    remain = deque()  # list
    # 봄
    while tree:
        # tmp, i, j = heapq.heappop(tree)
        tmp, i, j = tree.popleft()
        if graph[i][j] < tmp:
            dead.append((tmp//2, i, j))
        else:  # graph[i][j] >= tmp
            graph[i][j] -= tmp
            remain.append((tmp+1, i, j))
    
    # 여름
    while dead:
        adding, i, j = dead.popleft()
        graph[i][j] += adding
    
    # 가을
    while remain:
        is_five, i, j = remain.popleft()
        # heapq.heappush(tree, (is_five, i, j))
        tree.append((is_five, i, j))
        if is_five % 5 == 0:
            for l in range(8):
                nx, ny = i+dx[l], j+dy[l]
                if not in_range(nx, ny):
                    continue
                # heapq.heappush(tree, (1, nx, ny))  # tree에 넣음
                tree.appendleft((1, nx, ny))

    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += add[i][j]

print(len(tree))
"""