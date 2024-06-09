'''
[다리 만들기 2]
n by m, 땅(1)/바다(0)

다리는 바다에만 건설, 가로/세로
다리 길이는 차지하는 칸 수

다리를 연결해서 모든 섬을 연결
교차하는 경우에도 다리 길이 포함

[[0, 0, 0, 0, 0, 0, 1, 1], 
 [2, 2, 0, 0, 0, 0, 1, 1], 
 [2, 2, 0, 0, 0, 0, 0, 0], 
 [2, 2, 0, 0, 0, 3, 3, 0], 
 [0, 0, 0, 0, 0, 3, 3, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [4, 4, 4, 4, 4, 4, 4, 4]]
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < m

def dfs(x, y, cnt):
    graph[x][y] = cnt
    for l in range(4):
        nx, ny = x+dx[l], y+dy[l]
        if not in_range(nx, ny) or visited[nx][ny]:
            continue
        if graph[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt)

    return

k = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j, k)
            k += 1  # 5까지 기록됨

edge = set()

def distance(x, y, now):
    for l in range(4):
        cnt = 0  # 몇 칸 갔는지 체크
        nx, ny = x, y
        while in_range(nx+dx[l], ny+dy[l]):
            nx += dx[l]
            ny += dy[l]
            if graph[nx][ny] > 0 and graph[nx][ny] != now:
                if cnt >= 2:  # 다리 길이 최소 2칸 이상
                    edge.add((cnt, now, graph[nx][ny]))  # (cnt, now, next)
                break
            elif graph[nx][ny] == 0:
                cnt += 1
            else:  # ex. graph[nx][ny] == now
                break

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 :
            distance(i, j, graph[i][j])
            
parent = [i for i in range(k)]  # [0, 4+1]

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(parent):
    root = find_parent(1, parent)
    if all(find_parent(i, parent) == root for i in range(2, k)):
        return True
    return False

def main():
    answer = 0  # min
    for (cnt, now, nxt) in sorted(edge):  # 정렬!
        if find_parent(now, parent) != find_parent(nxt, parent):
            union_parent(now, nxt, parent)
            answer += cnt
    if check(parent):
        return answer
    else:
        return -1

print(main())

''' # 다른 사람의 풀이
def main():
    num = 0  # 간선 개수
    answer = 0  # min
    for (cnt, now, nxt) in sorted(edge):  # 정렬!
        if find_parent(now, parent) != find_parent(nxt, parent):
            union_parent(now, nxt, parent)
            answer += cnt
            num += 1
    return answer if (answer > 0) and (num == k-2) else -1

print(main())
'''