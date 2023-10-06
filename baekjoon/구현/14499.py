'''
[주사위 굴리기]
n by m, (r, c) : r 북쪽으로부터, c 서쪽으로부터
주사위를 놓은 곳의 좌표와 이동시키는 명령
주사위가 이동했을 때마다 상단에 쓰여있는 값?

- 가장 처음에는 주사위의 모든 면 0
- 이동한 칸에 쓰인 숫자가 0이면 바닥면이 복사
- 0이 아닌 경우 칸에 쓰여 있는 수가 바닥면에 복사
  & 칸에 쓰여 있는 수는 0이 됨!!! <- 여기서 틀림
'''
# 행, 열, 좌표 x, y, 명령 개수
n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# k : 동 1 서 2 북 3 남 4 (-1)
order = list(map(int, input().split()))

# 위 뒤 오 [1, 2, 3, 4, 5, 6] 왼 앞 아
# 동 [4, 2, 1, 6, 5, 3]
# 서 [3, 2, 6, 1, 5, 4]
# 북 [5, 1, 3, 4, 6, 2]
# 남 [2, 6, 3, 4, 1, 5]

dice = [0, 0, 0, 0, 0, 0]

   #  동 서 북 남 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(k):
   global dice
   a, b, c, d, e, f = map(int, dice)
   if k == 1:
      dice = [d, b, a, f, e, c]
   elif k == 2:
      dice = [c, b, f, a, e, d]
   elif k == 3:
      dice = [e, a, c, d, f, b]
   else:   # 4
      dice = [b, f, c, d, a, e]
       
for k in order:
   nx = x + dx[k-1]
   ny = y + dy[k-1]
   if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
   turn(k)
   if graph[nx][ny] == 0:
      graph[nx][ny] = dice[-1]  # 바닥면이 복사
   else:
      dice[-1] = graph[nx][ny]  # 바닥면에 복사
      graph[nx][ny] = 0  # 칸에 쓰여 있는 수 0
   print(dice[0])  # 맨 윗면 print
   x, y = nx, ny

