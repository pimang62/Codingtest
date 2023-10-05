from collections import deque

def solution(places):
    p_list = []  # P가 찍혀있는 좌표
    result = []  # 0 or 1 결과
    for place in places:
        graph = []   # 각 place의 graph
        for i in range(len(place)):
            row = []
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    p_list.append((i, j))
                row.append(place[i][j])
            graph.append(row)

        # [[0,0],[0,4],[2,1],[2,3],[4,0],[4,4]]
        
        def bfs(i, j):
            nonlocal graph
            visited = [[0]*len(place[0]) for _ in range(len(place))]
            
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            
            q = deque([(i, j)])
            visited[i][j] = 1
            
            while q:
                x, y = q.popleft()
                if visited[x][y] > 3:
                    break
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= len(place) or ny < 0 or ny >= len(place[0]):
                        continue
                    
                    if visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                        visited[nx][ny] += visited[x][y] + 1
                        q.append((nx, ny))
                    
                    if visited[nx][ny] >= 1 and (abs(nx-x)+abs(ny-y)) <= 2 and graph[nx][ny] == 'P':
                        return False
            return True
        
        cnt = 0 # 다른 P를 만난 횟수
        for (i, j) in p_list:
            if bfs(i, j) == False:
                cnt += 1
            
        result.append(0 if cnt > 0 else 1)

    return result

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))