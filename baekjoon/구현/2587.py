'''
[치킨 배달]
n by n, 1 by 1 크기
r행 c열 1부터 시작
0 빈 칸, 1 집, 2 치킨집
거리 측정: 맨하탄

수익을 많이 낼 수 있는 개수 최대 m개
도시의 치킨 거리가 작게 될지?

우선순위
- 치킨집 m개 남기기: 백트래킹
- 치킨 거리 구하기: 1을 기준
- 가장 거리 짧은 것 찾기
'''
from itertools import combinations

n, m = map(int, input().split())

record = [[1e9]*n for _ in range(n)]
ones = []
twos = []
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            ones.append((i, j))
        if row[j] == 2:
            twos.append((i, j))
    graph.append(row)
'''
result = 1e9  # 최소 치킨 거리
for combi in combinations(twos, m):
    answer = 0   # 각 combi별 answer
    for (ti, tj) in combi:
        record[ti][tj] = 2
        for (oi, oj) in ones:
            tmp = abs(ti-oi) + abs(tj-oj)
            if tmp < record[oi][oj]:
                record[oi][oj] = tmp
    
    for (oi, oj) in ones:
        answer += record[oi][oj]
    
    result = min(result, answer)
    
    record = [[1e9]*n for _ in range(n)]  # 초기화

print(result)
'''
result = 1e9  # 최소 치킨 거리
visited = [0]*len(twos)  # twos 배열 방문 여부
       
def dfs(cnt, idx):
    global result
    if cnt == m:
        # print(visited)
        # [1, 1, 0, 0, 0]
        # [1, 0, 1, 0, 0]
        # [1, 0, 0, 1, 0]
        # [1, 0, 0, 0, 1]
        # [0, 0, 0, ....]
        answer = 0
        for (oi, oj) in ones:
            dist = 1e9  # 최솟값 기록
            for k in range(len(twos)):
                if visited[k]:
                    ti, tj = twos[k]
                    tmp = abs(ti-oi)+abs(tj-oj)
                    dist = min(dist, tmp)
            answer += dist
        result = min(result, answer)
        return 
    
    for i in range(idx, len(twos)):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, i+1)  # not idx+1!!!
            visited[i] = 0
            
dfs(0, 0)
print(result)
