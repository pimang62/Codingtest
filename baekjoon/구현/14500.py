'''
[테트로미노]
정사각형 4개를 이어 붙인 폴리오미노 == 테트로미노
테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로!
회전이나 '대칭'을 시켜도 됨!

0 0 0 0    0 0 
           0 0
0    0    
0    0 0  0 0 0
0 0    0    0

  0    0
  0  0 0
0 0  0

[(x, y), (x, y+1), (x, y+2), (x, y+3)]
[(x, y), (x+1, y), (x+2, y), (x+3, y)]

[(x, y), (x, y+1), (x+1, y), (x+1, y+1)]

[(x, y), (x+1, y), (x+2, y), (x+2, y+1)]
[(x, y), (x, y+1), (x, y+2), (x+1, y)]
[(x, y), (x, y+1), (x+1, y+1), (x+2, y+1)]
[(x, y), (x+1, y), (x+1, y-1), (x+1, y-2)]
------------------------------------------
[(x, y), (x+1, y), (x+2, y), (x+2, y-1)]
[(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)]
[(x, y), (x, y+1), (x+1, y), (x+2, y)]
[(x, y), (x, y+1), (x, y+2), (x+1, y+2)]

[(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)]
[(x, y), (x, y+1), (x+1, y-1), (x+1, y)]
-----------------------------------------
[(x, y), (x+1, y), (x+1, y-1), (x+2, y-1)]
[(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)]

[(x, y), (x, y+1), (x, y+2), (x+1, y+1)]
[(x, y), (x+1, y), (x+2, y), (x+1, y-1)]
[(x, y), (x+1, y-1), (x+1, y), (x+1, y+1)]
[(x, y), (x+1, y), (x+2, y), (x+1, y+1)]
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0  # initialized
lego = [[(x, y), (x, y+1), (x, y+2), (x, y+3)],
        [(x, y), (x+1, y), (x+2, y), (x+3, y)],
        
        [(x, y), (x, y+1), (x+1, y), (x+1, y+1)],
        
        [(x, y), (x+1, y), (x+2, y), (x+2, y+1)],
        [(x, y), (x, y+1), (x, y+2), (x+1, y)],
        [(x, y), (x, y+1), (x+1, y+1), (x+2, y+1)],
        [(x, y), (x+1, y), (x+1, y-1), (x+1, y-2)],
        
        [(x, y), (x+1, y), (x+2, y), (x+2, y-1)],
        [(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)],
        [(x, y), (x, y+1), (x+1, y), (x+2, y)],
        [(x, y), (x, y+1), (x, y+2), (x+1, y+2)],
        
        [(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)],
        [(x, y), (x, y+1), (x+1, y-1), (x+1, y)],
        
        [(x, y), (x+1, y), (x+1, y-1), (x+2, y-1)],
        [(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)],
        
        [(x, y), (x, y+1), (x, y+2), (x+1, y+1)],
        [(x, y), (x+1, y), (x+2, y), (x+1, y-1)],
        [(x, y), (x+1, y-1), (x+1, y), (x+1, y+1)],
        [(x, y), (x+1, y), (x+2, y), (x+1, y+1)]]

def in_range(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    return False

answer = 0  # 최댓값 기록

def check(i, j):
    global answer
    for k in range(len(lego)):
        cnt = 0
        flag = True  # 끼워 넣을 수 있는지
        x, y = i, j
        for (dx, dy) in lego[k]:
            nx, ny = x+dx, y+dy
            if not in_range(nx, ny):
                flag = False
                break
            else:
                cnt += graph[nx][ny]
        if flag:
            answer = max(answer, cnt)
    
    return answer

for i in range(n):
    for j in range(m):
        check(i, j)
        
print(answer)