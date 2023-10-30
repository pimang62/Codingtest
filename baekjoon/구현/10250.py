'''
6*1 + 4
30*2 + 12

n // h = 1 +1 / 2 +1
n % h = 4 / 12

if n == 60:
    60//30 -> 2(x) -> 1!
    (60-1)//30 -> 1
'''

t = int(input())
    
def transform(num):
    if len(str(num)) < 2:
        return '0'+str(num)
    return str(num)
    
for _ in range(t):
    h, w, n = map(int, input().split())
    a, b = str((n-1)%h+1), transform((n-1)//h+1)
    print(a+b)  # str!
    