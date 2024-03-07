'''
[2021 KAKAO BLIND RECRUITMENT]
https://school.programmers.co.kr/learn/courses/30/lessons/72413

무지가 택시비를 아낄 방법
어피치와 귀가 방향이 비슷
택시 합승을 적절히 이용하면 택시 요금을 얼마나 아낄지?

출발 지점 s, A의 집 a, B의 집 b
예상 최저 택시요금 얼마?
(단, 각자 이동하는 경우 더 낮다면 합승 안함!)

fares: c-d 사이가 f원
왕복으로 비용 같음

graph = [
    [],
    [2, 3, 5],
    [4, 7],
    ...
]
'''
# 플로이드 워셜
def solution(n, s, a, b, fares):
    """
    # 0 -> 1e9로 바꿀것
    [[0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 41, 10, 24, 25], 
     [0, 0, 0, 22, 66, 0, 0], 
     [0, 41, 22, 0, 0, 24, 0], 
     [0, 10, 66, 0, 0, 0, 50], 
     [0, 24, 0, 24, 0, 0, 2], 
     [0, 25, 0, 0, 50, 2, 0]]
    """
    graph = [[1e9]*(n+1) for _ in range(n+1)]
    for [c, d, f] in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    answer = 1e9
    for i in range(1, n+1):  # 경유 지점 i
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    return answer

# 다익스트라
import heapq
def solution(n, s, a, b, fares):
    """
    [[],
     [(10,4),(41,3),(24,5),(25,6)],
     [(66,4),(22,3)],
     [(24,5),(41,1),(22,2)],
     [(10,1),(50,6),(66,2)],
     [(24,3),(2,6),(24,1)],
     [(2,5),(50,4),(25,1)],
    ]
    """
    graph = [[] for _ in range(n+1)]
    for [c, d, f] in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    
    def dijkstra(s):
        dist = [1e9]*(n+1)
        dist[s] = 0  # initialize
        
        q = []  
        heapq.heappush(q, (0, s))  # 시작 지점 밀어넣기
        while q:
            now_cost, now = heapq.heappop(q)
            for (nxt_cost, nxt) in graph[now]:
                if dist[nxt] < dist[now] + nxt_cost:  # 이미 작다면
                    continue
                dist[nxt] = min(dist[nxt], dist[now] + nxt_cost)
                heapq.heappush(q, (dist[nxt], nxt))
        
        return dist  # [1000000000.0, 10, 66, 51, 0, 34, 35]
    
    board = [[]]
    for i in range(1, n+1):
        board.append(dijkstra(i))  # 모든 노드에서 시작한 dijkstra 넣음
    
    answer = 1e9
    for k in range(1, n+1):
        answer = min(answer, board[s][k] + board[k][a] + board[k][b])
    
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))