'''
[너의 평점은]

'''
import math
dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

n = 20  # 평균
ans = 0  # 총점
summ = 0  # 학점의 총합
for _ in range(20):
    A, B, C = map(str, input().split())
    B = float(B)
    if C == 'P':
        n -= 1  # 세지 않음
        continue
    summ += B
    ans += dic[C]*B
    
print(f"{ans/summ:.6f}")