'''
[2048 (Easy)]
유의 사항
- 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없음
- 똑같은 수가 세 개 있는 경우 이동하려고 하는 쪽의 칸이 먼저

최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값?

# def check()
-> maxi = max(map(max, graph)) 대체

def move():
- i = 0, i를 i-1로(1~)
- j = 0, j를 j-1로(1~)
- i = n-1, i를 i+1로(n-2~)
- j = n-1, j를 j+1로(n-2~)

def bfs():

'''
from collections import deque 

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

def move(board, cnt):
    global q  # 그래프 후보 넣기
    
    # 북
    b1 = [[0]*n for _ in range(n)]
    for j in range(n):
        b = deque()  # 열 저장
        for i in range(n):
            if board[i][j] != 0:
                b.append(board[i][j])
        b_prime = []  
        idx = 0  # pointer
        while idx < len(b):
            if idx == len(b)-1:
                b_prime.append(b[idx])
                break
            if b[idx] == b[idx+1]:
                b_prime.append(2*b[idx])
                idx += 2
            else:
                b_prime.append(b[idx])
                idx += 1

        blist = b_prime + [0]*(n-len(b_prime))
        
        for i in range(n):
            b1[i][j] = blist[i]
    
    q.append((b1, cnt+1))

    # 서
    b2 = []
    for i in range(n):
        b = deque()  # 행 저장 : [8, 2, 2, 4]
        for j in range(n):
            if board[i][j] != 0:
                b.append(board[i][j])
        b_prime = []  
        idx = 0  # pointer
        while idx < len(b):
            if idx == len(b)-1:
                b_prime.append(b[idx])
                break
            if b[idx] == b[idx+1]:
                b_prime.append(2*b[idx])
                idx += 2
            else:
                b_prime.append(b[idx])
                idx += 1

        # [4, 2, 0]
        blist = b_prime + [0]*(n-len(b_prime))
        
        # [[4, 2, 0], ...]
        b2.append(blist)
    
    q.append((b2, cnt+1))
    
    # 남
    b3 = [[0]*n for _ in range(n)]
    for j in range(n):
        b = deque()  # 열 저장
        for i in range(n-1, -1, -1):
            if board[i][j] != 0:
                b.append(board[i][j])
        b_prime = []  
        idx = 0  # pointer
        while idx < len(b):
            if idx == len(b)-1:
                b_prime.append(b[idx])
                break
            if b[idx] == b[idx+1]:
                b_prime.append(2*b[idx])
                idx += 2
            else:
                b_prime.append(b[idx])
                idx += 1
        
        blist = b_prime + [0]*(n-len(b_prime))

        for i in range(n-1, -1, -1):  # 2 1 0
            b3[i][j] = blist[-i-1]  # -3 -2 -1
    
    q.append((b3, cnt+1))
    
    # 동
    b4 = []
    for i in range(n):
        b = deque()  # 행 저장 : [2, 2, 2]
        for j in range(n-1, -1, -1):
            if board[i][j] != 0:
                b.append(board[i][j])
        b_prime = []  
        idx = 0  # pointer
        while idx < len(b):
            if idx == len(b)-1:
                b_prime.append(b[idx])
                break
            if b[idx] == b[idx+1]:
                b_prime.append(2*b[idx])
                idx += 2
            else:
                b_prime.append(b[idx])
                idx += 1

        # [4, 2, 0]
        blist = b_prime + [0]*(n-len(b_prime))
        
        # [[0, 2, 4], ...]
        b4.append([blist[i] for i in range(n-1, -1, -1)])
    
    q.append((b4, cnt+1))


def bfs():
    global q
    answer = max(map(max, graph))  # 최댓값
    
    board = graph  # initialize
    cnt = 0  # 시도 횟수
    move(board, cnt)  
    
    while q:
        board, cnt = q.popleft()
        answer = max(answer, max(map(max, board)))
        if cnt > 5:
            return answer
        move(board, cnt)
     
print(bfs())

# b = deque(map(int, input().split()))
# b_prime = []
# idx = 0
# while idx < len(b):
#     if idx == len(b)-1:
#         b_prime.append(b[idx])
#         break
#     if b[idx] == b[idx+1]:
#         b_prime.append(2*b[idx])
#         idx += 2
#     else:
#         b_prime.append(b[idx])
#         idx += 1
        
# print(b_prime)

# [다른 사람의 풀이]
# 출처 : https://jeongchul.tistory.com/667
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()

def get(i, j):
    if board[i][j]: # 0이 아닌 값이라면
        q.append(board[i][j]) # queue에 board의 값을 넣는다.
        board[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트
        
def merge(i, j, di, dj): # row index, column index, y방향, x방향 
    while q:
        x = q.popleft() # 움직이려는 블록 값을 가져온다. FIFO 
        if not board[i][j]: # 0이라면 그대로 놓는다.
            board[i][j] = x
        elif board[i][j] == x: # 값이 일치한다면
            board[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj 
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj
            board[i][j] = x 

def move(k):
    # board[i][j]
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
    elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
    elif k == 2: # 오른쪽으로 이동, column index는 0
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
    else: # 왼쪽으로 이동, column index는 n-1
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동
            
def solve(count):
    global board, answer
    if count == 5: # 최대 5번까지 움직였다면
        for i in range(n):
            answer = max(answer, max(board[i])) # 가장 큰 값이 answer
        return
    b = [x[:] for x in board] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
    
    for k in range(4): # 4방향으로 움직인다.
        move(k) # 움직인다.
        solve(count+1) # 재귀적으로 호출한다.
        board = [x[:] for x in b]

solve(0)
print(answer)