n = int(input())
plans = list(input().split())

rule = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]              # (1, 2) -> 'R' -> (1, 3) : 행렬 이동임
dy = [-1, 1, 0, 0]  

x = 1       # 첫 좌표
y = 1

for plan in plans:
    for i in range(len(rule)):
        if plan == rule[i]:
            # 조건에 맞는 이동을 해야할 경우 
            # 좌표를 따로 두는게 좋음 !
            nx = x + dx[i]
            ny = y + dy[i]
    # 제한 조건 확인
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    # 최종 이동
    x, y = nx, ny

print(x, y)
