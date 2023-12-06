'''
[삼각형 외우기]
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
'''
from collections import defaultdict

d = defaultdict(int)
for _ in range(3):
    num = int(input())
    d[num] += 1

summ = 0
for k, v in d.items():
    summ += k*v

if (summ == 180) and (len(d) == 1):
    print('Equilateral')
elif (summ == 180) and (len(d) == 2):
    print('Isosceles')
elif (summ == 180) and (len(d) == 3):
    print('Scalene')
else:  # sum(d.keys()) != 180
    print('Error')