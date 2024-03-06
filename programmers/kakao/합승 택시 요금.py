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
answer_a = 1e9
answer_b = 1e9

def dfs(now, target, total, updated_fares):  # now: [66, 4], target : a or b, 70
    global answer_a, answer_b
    if now[1] == target:
        if str(target) == 'a':
            answer_a = min(answer_a, total+now[0])
        else:  # 'b'
            answer_b = min(answer_b, total+now[0])
        return
    
    for nxt in updated_fares[now[1]]:
        if nxt and nxt[1] != 0:  # 방문하지 않았다면
            ori_nxt = nxt
            nxt[1] = 0  # 방문 처리
            dfs(nxt, target, total+nxt[0], updated_fares)
            nxt = ori_nxt


def solution(n, s, a, b, fares):
    '''
    [[],
     [[10,4],[41,3],[24,5],[25,6]],
     [[66,4],[22,3]],
     [[24,5],[41,1],[22,2]],
     [[10,1],[50,6],[66,2]],
     [[24,3],[2,6],[24,1]],
     [[2,5],[50,4],[25,1]],
    ]
    '''
    graph = [[] for _ in range(n+1)] 
    for [c, d, f] in fares:  # 1-indexed
        graph[c].append([f, d])
        graph[d].append([f, c])
    
    dfs(s, a, 0, fares)
    dfs(s, b, 0, fares)
    print(answer_a)
    print(answer_b)
    return answer_a + answer_b
    