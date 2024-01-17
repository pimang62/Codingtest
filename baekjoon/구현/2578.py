'''
[빙고]
5 by 5, 5줄 graph, 5줄 사회자
몇 번째 수를 부른 후 "빙고"를 외치게 되는지?

25*25
'''
# graph = [list(map(int, input().split())) for _ in range(5)]

board = [[0]*5 for _ in range(5)]

d = {}
for i in range(5):
    row = input().split()
    for j in range(5):
        d[row[j]] = (i, j)

def check():
    cnt = 0  # 3개 이상
    # 행 확인
    for i in range(5):
        check = True
        for j in range(5):
            if board[i][j] == 0:
                check = False
                break
        if check:
            cnt += 1
    # 열 확인
    for j in range(5):
        check = True
        for i in range(5):
            if board[i][j] == 0:
                check = False
                break
        if check:
            cnt += 1
    # 왼쪽 대각선
    for i in range(5):
        check = True
        if board[i][i] == 0:
            check = False
            break
    if check:
        cnt += 1
    # 오른쪽 대각선
    for i in range(5):
        check = True
        if board[i][4-i] == 0:
            check = False
            break
    if check:
        cnt += 1
    # 아무것도 없으면
    return True if cnt >= 3 else False

def solution():
    for x in range(5):
        row = input().split()
        for y in range(5):
            if row[y] not in d:
                continue
            (i, j) = d[row[y]]
            board[i][j] = 1
            if check():
                return 5*x + (y+1)

print(solution())

""" 
[['11', '12', '2', '24', '10'], 
 ['16', '1', '13', '3', '25'], 
 ['6', '20', '5', '21', '17'], 
 ['19', '4', '8', '14', '9'], 
 ['22', '15', '7', '23', '18']]
 
{'11': (0, 0), '12': (0, 1), '2': (0, 2), '24': (0, 3), '10': (0, 4), 
 '16': (1, 0), '1': (1, 1), '13': (1, 2), '3': (1, 3), '25': (1, 4), 
 '6': (2, 0), '20': (2, 1), '5': (2, 2), '21': (2, 3), '17': (2, 4), 
 '19': (3, 0), '4': (3, 1), '8': (3, 2), '14': (3, 3), '9': (3, 4), 
 '22': (4, 0), '15': (4, 1), '7': (4, 2), '23': (4, 3), '18': (4, 4)}
"""