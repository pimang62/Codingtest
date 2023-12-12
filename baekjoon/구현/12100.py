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
# 출처 : https://www.acmicpc.net/board/view/113931
import sys
from copy import deepcopy
input = sys.stdin.readline
global N
global _map
global perm_array
global my_max
my_max =[]
N = int(input())
_map = [list(map(int, input().split())) for _ in range(N)]
perm_array = []


def my_perm(cnt, arr):
    global N
    global _map
    global my_max
    if cnt == 5:
        my_map = [_m[:] for _m in _map[:]]
        # 0 상 1하 2좌 3우
        for dir in arr:
            go(my_map, N, dir)
#-------------------------------------------------------------------
        #my_max = max(max(max(my_map)), my_max)
        my_max.append(max(map(max,my_map)))
#-------------------------------------------------------------------
        return


    for i in range(4):
        my_perm(cnt + 1, arr + [i])


# dir 0 상 1 하 2 좌 3 우
def go(board, n, dir):
    if dir == 0:
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    # 포인터가 가리키는 수가 0일 때
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                    # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
    if dir == 1:

        for j in range(n):
            pointer = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    if dir == 2:

        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    if dir == 3:

        for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp


my_perm(0, [])
print(max(my_max))