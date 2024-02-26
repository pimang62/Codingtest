'''
[킹]
8 by 8 체스판, 킹 하나
킹의 현재 위치 주어짐

알파벳(A-H)은 열, 숫자(1-8)는 행

- R: right
- L: left
- B: below
- T: top
- RT: right top
- LT: left top
- RB: right below
- LB: left below

돌이 하나 있고, 돌과 같은 곳으로 이동할 때는 
돌을 같은 방향으로 한 칸 이동 시킴

범위 밖으로 나갈 경우 그 이동은 건너 뛰고 다음 이동
킹과 돌의 마지막 위치?
'''
king, stone, N = map(int, input().split())

r = {"A":0, "B":, "C", "D", "E", "F", "G", "H"}
c = {"1", "2", "3", "4", "5", "6", "7", "8"}

d = {"R":(0, 1), "L":(0, -1), "B":(1, 0), "T":(-1, 0), 
     "RT":(-1, 1), "LT":(-1, -1), "RB":(1, 1), "LB":(1, -1)}

for _ in range(N):
    order = input()

