"""
미로탈출

N X M의 맵이 있다. 유저는 (1,1)에 위치하고 맵의 출구는 (N,M)에 위치한다.
이때 맵에 몬스터가 있어 갈 수 없는 부분이 있는데, 이것은 0으로 표시된다.
그 외에 몬스터가 없어서 갈 수 있는 부분은 1로 표시된다.
유저가 맵을 빠져나오기 위해 움직여야 하는 최소 칸의 개수를 구하여라

입력:
5 6
101010
111111
000001
111111
111111

출력:
10
"""
from collections import deque

# 입력받기
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

# 방향벡터 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 큐 선언, 최초 위치 큐에 삽입, 방문처리
queue = deque()
queue.append((0,0))

# BFS 큐 순회 시작
while queue:
    # 첫 요소 추출
    v = queue.popleft()

    # 갈 수 있는 모든 옵션 순회
    for i in range(len(dx)):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]

        # 조건을 만족하지 않는다면 continue
        if nx >= n or ny >= m or nx < 0 or ny < 0 or array[nx][ny] == 0:
            continue
        # 만약 조건을 만족하면 방문처리
        elif array[nx][ny] == 1:
            array[nx][ny] = array[v[0]][v[1]] + 1
            # 큐에 삽입
            queue.append((nx, ny))

# (n-1,m-1) 프린트
print(array[n-1][m-1])