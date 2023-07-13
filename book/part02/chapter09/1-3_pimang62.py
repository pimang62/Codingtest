'''
[플로이드 워셜 알고리즘]
2차원 테이블 설정

총 n번 수행
1번 노드를 거쳐가는 점화식 : a_23 = min(a_23, a_21 + a_13)
                            a_24 = min(a_24, a_21 + a_24)
                            ... 3P2 = 6가지 경우
2번 노드를 거쳐가는 점화식 : a_13 = min(a_13, a_12 + a_23)
                            ...
...

a_ab = min(a_ab, a_ak + a_kb)
'''

INF = int(1e9)

# 노드, 간선
n = int(input())
m = int(input())

# 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # 1번 노드에 연결된 2번 노드 비용 c 업데이트
    graph[a][b] = c    

# 자기 자신 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 플로이드 워셜 알고리즘 : 점화식 작성
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 모든 노드로 가는 2차원 그래프 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    # 한 줄 띄기
    print()