'''
[앵무새]
순서 지키며 반복
3
S = [
      [i want 'to' 'see' 'you']
      [next 'week']
      [good 'luck']
     ]

target = [
      [i want next good 'luck' 'week' 'to' 'see' 'you']
    ]
'''
n = int(input())

S = []
for _ in range(n):
    S.append(input().split())
    
target = input().split()

for t in range(len(target)-1, -1, -1):
    flag = False
    for i in range(len(S)):
        if S[i] and (S[i][-1] == target[t]):
            flag = True
            S[i].pop()
    if not flag:
        print('Impossible')
        break

if flag:
    print('Possible')
        
    