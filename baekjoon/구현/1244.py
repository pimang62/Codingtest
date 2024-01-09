'''
[스위치 켜고 끄기]
- 남학생은 스위치 번호가 자기가 받은 수의 배수이면 상태 바꿈
- 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
  좌우 대칭이면서 가장 많은 스위치 포함 -> 모두 바꿈 : 항상 홀수

스위치 개수 <= 100, 학생 수 <= 100 -> 1e4
남 1, 여 2 -> 따로 함수 두기

8
0 1 0 1 0 0 0 1
2
1 3
2 3

* output: 한 줄에 20개씩 출력!
'''
n = int(input())  # <= 100
nlist = list(map(int, input().split()))

def in_range(a):
    if 0 <= a < n:
        return True
    return False

def boy(num):
    global nlist
    idx = num-1
    mul = 2
    while idx < n:
        nlist[idx] ^= 1  # 0 xor 1 : 1, 1 xor 1 : 0
        idx = num*mul -1 
        mul += 1
    
def girl(num):
    global nlist
    idx = num-1
    sub = 1  # 더하거나 빼질 수
    nlist[idx] ^= 1
    while True:
        if not in_range(idx-sub) or not in_range(idx+sub):
            return
        if nlist[idx-sub] != nlist[idx+sub]:
            return 
        nlist[idx-sub] ^= 1  # 반전(뒤집기)
        nlist[idx+sub] ^= 1
        sub += 1    

s = int(input())  # student
for _ in range(s):
    typ, num = map(int, input().split())
    if typ == 1:
        boy(num)
    else:
        girl(num)

if n > 20:  # output: 한 줄에 20개씩 출력!
    a, b = divmod(n, 20)
    for i in range(0, n-b, 20):
        print(*nlist[i:i+20])
    print(*nlist[n-b:])
else:
    print(*nlist)