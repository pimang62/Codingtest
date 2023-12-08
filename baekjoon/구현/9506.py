'''
[약수들의 합]
...
-1
{n} =  + + +
{n} is NOT perfect.
'''
import math
def find(n):
    ans = set()  # 약수들
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if i == 1:  # 자기 자신 포함 안하게!
                ans.add(i)
                continue
            ans.add(i)
            ans.add(n//i)
    return sorted(ans)  # 오름차순

while True:
    num = int(input())
    if num == -1:
        break
    res = find(num)  # list of 약수
    print(res)
    if num == sum(res):
        print(f"{num} =", ' + '.join(str(a) for a in res))
    else:
        print(f"{num} is NOT perfect.")