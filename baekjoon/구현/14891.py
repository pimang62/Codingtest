'''
[톱니바퀴]
톱니바퀴 A를 회전할 때 B와 맞닿은 극이 다르다면 -> 반대로 회전
극이 같으면 움직이지 않음!!

12시 방향부터 시계 방향 순서대로 주어진다.
N극은 0 S는 1

회전 횟수 k
번호, 방향(1 시계 -1 반시계)

0 1 (2) 3 4 5 (6) 7
1: 0 1 (2) 3 4 5 6 7
2: 0 1 [2] 3 4 5 (6) 7
3: 0 1 "2" 3 4 5 [6] 7
4: 0 1 2 3 4 5 "6" 7

점수 [0]

- 다른 극이면 무조건 반대로 움직임
- 같은 극이면 움직이지 않음 
 : 반대 방향으로 갈 수 있는지 확인하고, 돌림

rotate(양수) : 오른쪽 ex.rotate(2) : 2칸 오른쪽
rotate(음수) : 왼쪽   ex.rotate(-2) : 2칸 왼쪽
'''
from collections import deque

#{1: deque([1, 0, 1, 0, 1, 1 ,1, 1]), ...
n_dict = {i:deque([int(s) for s in input()]) for i in range(1, 5)}
d_dict = {1:1, 2:2, 3:4, 4:8}  # 방향에 따른 S극 점수

def rotate_left(num, dirc):
    if num < 1 or n_dict[num][2] == n_dict[num+1][6]:
        return  # 범위 밖이거나 왼쪽 2와 오른쪽 6이 같을 때
    if n_dict[num][2] != n_dict[num+1][6]:
        rotate_left(num-1, -dirc)
        n_dict[num].rotate(dirc)

def rotate_right(num, dirc):
    if num > 4 or n_dict[num-1][2] == n_dict[num][6]:
        return  # 범위 밖이거나 왼쪽 2와 오른쪽 6이 같을 때
    if n_dict[num-1][2] != n_dict[num][6]:
        rotate_right(num+1, -dirc)
        n_dict[num].rotate(dirc)
    
k = int(input())
for _ in range(k):
    (n, d) = map(int, input().split())
    rotate_left(n-1, -d)
    rotate_right(n+1, -d)
    n_dict[n].rotate(d)

score = 0 
for n in range(1, 5):
    if n_dict[n][0] == 0:
        continue
    else: score += d_dict[n] 
    
print(score)