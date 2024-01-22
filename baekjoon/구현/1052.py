'''
[물병]
1 1 1 1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 1 + 1 : 이진법 나머지 1
4 4 4 2 + 2
8 8
16

13 : 1101
  -> %2 +1
14 : 1110
  -> %2 +1
15 : 1111
  -> %2 +1
16 : 10000
  -> %2 //

'''
n, k = map(int, input().split())

s = bin(n)[2:]

answer = 0
while s.count('1') > k:
    n += 1
    answer += 1
    s = bin(n)[2:]

print(answer)