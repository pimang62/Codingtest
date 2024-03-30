'''
[자리배정]
r by c, 왼쪽 아래 (1, 1)
시계방향으로 좌석 배정

대기 순서가 k인 관객의 번호 (x, y)

(1 6) 
(1 5) 
(1 4)
(1 3)
(1 2) 
(1 1) (2 1) (3 1) (4 1) (5 1) (6 1) (7 1)

6	7	8	9	10	11	12
5	26	27	28	29	30	13
4	25	38	39	40	31	14
3	24	37	42	41	32	15
2	23	36	35	34	33	16
1	22	21	20	19	18	17
--------------------------
1	22	21	20	19	18	17
2	23	36	35	34	33	16
3	24	37	42	41	32	15
4	25	38	39	40	31	14
5	26	27	28	29	30	13
6	7	8	9	10	11	12

(1, 1) (2, 1) (3, 1) ...
(1, 2)
(1, 3)
...
(1, 6) (2, 6) (3, 6) ...
'''
c, r = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)
    exit()

dx = [1, 0, -1, 0]  # 남 동 북 서
dy = [0, 1, 0, -1]

x, y = 0, 0
D = 0  # direction

def in_range(tx, ty):
    return 0 <= tx < r and 0 <= ty < c

path = set()
path.add((0, 0))
cnt = 1  # 순서
while True:
    if cnt >= k:
        break 
    
    while (x+dx[D], y+dy[D]) not in path and in_range(x+dx[D], y+dy[D]):
        x += dx[D]
        y += dy[D]
        cnt += 1
        path.add((x, y))
        if cnt >= k:
            break 
    
    D = (D+1) % 4

print(y+1, x+1)


