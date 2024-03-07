'''
[킹]
8 by 8 체스판, 킹 하나
킹의 현재 위치 주어짐

알파벳(A-H)은 열, 숫자(1-8)는 행
왼쪽 아래가 A1

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
king, stone, N = input().split()
N = int(N)

r = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}  # 행
c = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}  # 열

kx, ky = r[king[1]], c[king[0]]  # 7, 0
sx, sy = r[stone[1]], c[stone[0]]  # 6, 0

d = {"R":(0, 1), "L":(0, -1), "B":(1, 0), "T":(-1, 0), 
     "RT":(-1, 1), "LT":(-1, -1), "RB":(1, 1), "LB":(1, -1)}

def in_range(a, b):
     if 0 <= a < 8 and 0 <= b < 8:
          return True
     return False

for _ in range(N):
     order = input()
     if in_range(kx+d[order][0], ky+d[order][1]):  # 킹이 범위 안에 있고
          if (kx+d[order][0], ky+d[order][1]) != (sx, sy):  # stone과 겹치지 않다면
               kx += d[order][0]
               ky += d[order][1]
          else:  # (kx+d[order][0], ky+d[order][1]) == (sx, sy)
               if in_range(sx+d[order][0], sy+d[order][1]):  # stone먼저 옮기고
                    sx += d[order][0]
                    sy += d[order][1]
                    kx += d[order][0]
                    ky += d[order][1]
               else: 
                    continue

r_rev = {v: k for k, v in r.items()}
c_rev = {v: k for k, v in c.items()}

print(''.join([c_rev[ky], r_rev[kx]]))  # 알파벳 먼저
print(''.join([c_rev[sy], r_rev[sx]]))




