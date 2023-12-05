'''
[진법 변환]

'''
zinbub = {str(i): i for i in range(10)}
alpha = {chr(i):i-55 for i in range(65, 91)}

zinbub.update(alpha)  # dict 합치기

N, B = input().split()
B = int(B)  # 진법

ans = 0  # 10진법
for i in range(len(N)):
    ans += zinbub[N[i]]*B**(len(N)-1-i)  # 35*36**4
    
print(ans)