'''
[계단 오르기]
- 계단은 한 번에 한 계단 / 두 계단씩
- 연속된 세 개의 계단을 밟아서는 안 됨
- 마지막 도착 계단은 반드시 밟아야 함

총 점수의 최댓값?

입력)
n = int(input())
table = []
for _ in range(n):
    table.append(int(input()))
'''
n = int(input())
table = []
for _ in range(n):
    table.append(int(input()))

#    10  20  15  25  10  20
# 0  10  30  35  50  65  65
# 1   0  20  25  55  45  75

# 1칸 : d[i][0] += d[i-1][2]
# 2칸 : d[i][1] += max(d[i-2][0], d[i-2][1])

d = [ [0]*n for _ in range(2) ]

if n == 1: print(table[0])
if n == 2: print(table[0]+table[1])   # 2칸보다 합이 당연히 최대

if n > 2:
    # 초기화
    d[0][0] = table[0]
    d[0][1] = table[0] + table[1]
    d[1][1] = table[1]

    for i in range(2, len(table)):
        d[0][i] = d[1][i-1] + table[i]     # 2칸에서 온 1칸
        d[1][i] = max(d[0][i-2], d[1][i-2]) + table[i]    # 1칸 or 2칸에서 온 2칸

    print(max(d[0][-1], d[1][-1]))
