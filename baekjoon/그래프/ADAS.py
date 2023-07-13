'''
*w by h, 0-indexed
s에서 시작 e로 도착
이동 후보 정점 목록 추가

우선순위
1. e
2. p-
3. 일반점

우선순위 같으면
1. a가 작은 것이 우선, a가 같으면 b가 작은 것이 우선
순서 : (a-1, b) 북, (a, b-1) 서, (a, b+1) 동, (a+1, b) 남

입력)
w, h = map(int, input().split())

graph = []
start = []
end = []

for i in range(w):
	row = input()
	for j in range(len(row)):
		if row[j] == "S":
			start.append((i, j))
		if row[j] == "E":
			end.append((i, j))
	graph.append([j for j in row])
			
	
'''
from heapq import heappush, heappop

w, h = map(int, input().split())

graph = []
count = [ [0]*h for _ in range(w) ]	# 점수 계산 테이블
visited = [ [False]*h for _ in range(w) ]

for i in range(w):
	row = input()
	for j in range(len(row)):
		if row[j] == "S":
			start = (-2, i, j)
		if row[j] == "E":
			end = (-2, i, j)
		#if row[j] == "P":
			#count[i][j] = -3
	graph.append([j for j in row])

	
def check(x, y, graph):
	
	c = 0		# P점의 개수 
	for (nx, ny) in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
		if nx < 0 or nx >= w or ny < 0 or ny >= h:
			continue
		if graph[nx][ny] == 'P':
			c += 1	
	return c


def bfs(_, i, j, graph, count):
	
	q = []
	heappush(q, (_, i, j))
	danger = 0
	while q:
		_, x, y = heappop(q)
		danger = count[x][y]
		for (nx, ny) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
			if nx < 0 or nx >= w or ny < 0 or ny >= h:
				continue
			if graph[nx][ny] == 'E':
				visited[nx][ny] = True
				heappush(q, (-2, nx, ny))
				count[nx][ny] = count[x][y]
				break
			if graph[nx][ny] == 'P' and visited[nx][ny] == False:
				visited[nx][ny] = True
				heappush(q, (-1, nx, ny))
				count[nx][ny] += check(nx, ny, graph)-3 + danger
			if graph[nx][ny] == '0' and visited[nx][ny] == False:
				visited[nx][ny] = True
				heappush(q, (0, nx, ny))
				count[nx][ny] += check(nx, ny, graph) + danger
			

	_, a, b = end
	return count[a][b]


(_, i, j) = start
visited[i][j] = True

print(bfs(_, i, j, graph, count))
