'''
[경사로]
n by n, 각 칸에는 높이
지나갈 수 있는 "길"이 몇 개 있는지?
- 한 행 또는 한 열 전부

행 열 각각 합쳐 총 2n개
지나갈 수 있으려면 모든 칸의 높이가 같아야!
또는 경사로를 놓아 지나감
- L개의 연속된 칸에 위 아래 칸이 1 차이 나는 곳에서!
- 낮은 칸의 높이는 모두 같아야 함

그러나
- 차이가 1이 아니거나 L개가 연속되지 않거나 
- 범위를 벗어나면 놓을 수 없음
- 놓은 곳에 또 놓거나 겹쳐도 놓을 수 없음

1. 나보다 작은 값이 나타난 경우
    - L만큼 앞이 같은 길이(나-1)인지 확인
      (가능하면 브릿지 있는지 보고 기록)
2. 나보다 큰 값이 나타난 경우
    - 1 초과의 큰 값이면 no
    - 나 포함 뒤로 L만큼 가능한지 확인
      (가능하면 브릿지 있는지 보고 기록)
3. 나랑 같은 값이면 그냥 지나감

* 참고 : https://sapjilkingios.tistory.com/entry/Python%EA%B5%AC%ED%98%84-%EB%B0%B1%EC%A4%80-14890%EB%B2%88-%EA%B2%BD%EC%82%AC%EB%A1%9C
'''
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(a):
    if 0 <= a < n:
        return True
    return False

def check(_list):
    visited = [0]*n
    for i in range(n-1):
        # 이 다음 값이 더 작을 때
        if _list[i] > _list[i+1]:  
            # 나 제외 내 앞에 l만큼
            for j in range(i+1, i+l+1):
                # 범위를 벗어나거나 방문한 적이 있으면 False
                if not in_range(j) or visited[j]:  
                    return False
                # 차이가 1보다 크면 False
                if (_list[i] - _list[j]) > 1:  
                    return False
                if not visited[j] and _list[j] == (_list[i]-1):
                    visited[j] = 1  # 방문 기록
        # 이 다음 값이 더 클 때
        elif _list[i] < _list[i+1]:
            # 나 포함 내 뒤에 l만큼
            for j in range(i-l+1, i+1):
                # 범위를 벗어나거나 방문한 적이 있으면 False
                if not in_range(j) or visited[j]:  
                    return False
                # 차이가 1보다 크면 False
                if (_list[i+1] - _list[j]) > 1:  
                    return False
                if not visited[j] and _list[j] == _list[i]:
                    visited[j] = 1  # 방문 기록
    return True


answer = 0  # 지나갈 수 있는 길 cnt

# 행 check
for row in graph:
    if check(row):
        answer += 1
        
# 열 check
for j in range(n):
    column = []
    for row in graph:
        column.append(row[j])
    if check(column):
        answer += 1

print(answer)