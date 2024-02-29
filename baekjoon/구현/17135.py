'''
[캐슬 디펜스]
n by m, n번행의 바로 아래(n+1)의 모든 칸에는 성이 존재
성을 지키기 위해 궁수 3명 배치, 한 칸에 최대 1명

각각의 턴마다 궁수는 적 하나 공격, 동시 공격

거리가 d이하인 적 중에서 가장 가까운 적 공격
여럿일 경우 가장 왼쪽에 있는 적 공격

같은 적이 여러 궁수에게 공격 당할 수 있음
공격받은 적은 게임에서 제외

공격이 끝나면 적이 이동, 아래로 한 칸
성이 있는 칸으로 이동하면 제외, 격자판 벗어나도 제외

거리는 맨하탄 거리, "궁수의 위치 중요"
제거할 수 있는 최대 적의 수?

0은 빈 칸, 1은 적이 있는 칸

1. 궁수 그리디 배치
    2. d만큼의 거리에 1 있는지 확인 후 0
    3. 적들 아래 칸으로 내림

5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
3

5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
3

5 5 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
5

5 5 5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
15

6 5 1
1 0 1 0 1
0 1 0 1 0
1 1 0 0 0
0 0 0 1 1
1 1 0 1 1
0 0 1 0 0
9

6 5 2
1 0 1 0 1
0 1 0 1 0
1 1 0 0 0
0 0 0 1 1
1 1 0 1 1
0 0 1 0 0
14
'''
from copy import deepcopy
from itertools import combinations

n, m, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0  # 처리한 적의 수

def _move(graph):
    new_graph = [[0]*m for _ in range(n)]
    for j in range(m):
        if graph[-1][j] == 1:
            for i in range(n):
                new_graph[i][j] = graph[i][j]
        else:  # == 0
            for i in range(n-1):
                new_graph[i+1][j] = graph[i][j]
    return new_graph

def _combinations(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in _combinations(array[i+1:], r-1):
                yield [array[i]] + next

class Solution:
    def __init__(self, board):
        self.board = board

    def move(self):
        new_board = [[0]*m]
        for i in range(n-1):
            new_board.append(self.board[i])
        
        self.board = new_board
        return
        # self.board = [[0]*m] + self.board[:-1]
        # return

    def attack(self, idxes):  # 열 좌표
        cnt = 0  # 현재 처리한 적의 수
        attack_list = []
        for idx in idxes:
            candidate = []
            for i in range(n):
                for j in range(m):
                    distance = (abs(i-n) + abs(j-idx))
                    if self.board[i][j] and distance <= d:
                        candidate.append((distance, i, j))

            if candidate:  # 후보가 있다면
                candidate.sort(key=lambda x: (x[0], x[2]))  # 거리가 가장 작고 왼쪽 우선
                attack_list.append(candidate[0])

        for a in attack_list:
            (_, x, y) = a
            if self.board[x][y]:  # == 1
                self.board[x][y] = 0
                cnt += 1
        
        return cnt

    def is_empty(self):
        for i in range(n):
            for j in range(m):
                if self.board[i][j]:  # == 1
                    return False
        return True
        # return all(cell == 0 for row in self.board for cell in row)


for combi in combinations(range(m), 3):
    board = deepcopy(graph)
    s = Solution(board)
    tmp = 0
    while not s.is_empty():
        tmp += s.attack(combi)
        s.move()

    answer = max(answer, tmp)

print(answer)