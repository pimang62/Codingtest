'''
[여행경로]
항상 "ICN" 공항에서 출발
방문하는 공항 경로를 배열에 담아 return

- 주어진 항공권을 모두 사용
- 가능한 경로가 2개 이상일 경우 sort, 앞서는 경로
- 모든 도시를 방문할 수 없는 경우는 주어지지 않음!
'''

result = None

def dfs(boarding, visited, answer, cnt):
    global result
    if len(answer) == cnt:
        result = answer[:]
        return

    target = answer[-1]
    if target not in boarding:  # 도착지점이 시작지점에 없을 때
            return
        
    for i in range(len(boarding[target])):  # [elist]
        
        if not visited[target][i]:  # 0이면
            answer += [boarding[target][i]]
            visited[target][i] = 1
        
            dfs(boarding, visited, answer, cnt)
            if result:  # 가장 우선 순위에 있는 result가 기록돼 있으면
                break
        
            answer.pop()
            visited[target][i] = 0
    
    return
    

def solution(tickets):
    
    boarding = {}  # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    visited = {}  # {'ICN': [0, 0], 'SFO': [0], 'ATL': [0, 0]}
    for [start, end] in tickets:
        boarding[start] = boarding.get(start, []) + [end]  # list로 초기화, end를 담음
        visited[start] = visited.get(start, []) + [0]  # [0, 0] 형태로

    # 알파벳 오름차순 정렬
    for key in boarding.keys():
        boarding[key].sort()
    
    dfs(boarding, visited, ["ICN"], len(tickets)+1)  # cnt는 freeze
    
    return result
    
    
# print(solution(tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution(tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution(tickets=[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))  # 예외 처리 반례!