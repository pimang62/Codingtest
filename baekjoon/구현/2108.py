'''
[통계학]
1. 산술평균 : 평균
2. 중앙값 : 오름차순, 가장 중앙
3. 최빈값 : 가장 많이  
4. 범위 : 최댓값-최솟값

'''
import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())  # 홀수 

n_list = []  # 13589
n_dict = defaultdict(int)
for _ in range(n):
    i = int(input())
    n_list.append(i)
    n_dict[i] += 1

n_list.sort()
n_dict = dict(sorted(n_dict.items()))

print(round(sum(n_list)/n))  # 산술평균
print(n_list[n//2])   # 중앙값 5 -> 2

cnt, max_val, mode = 0, max(n_dict.values()), 0 # 두 번째로 작은 값 if cnt == 2
mini, maxi = 1e9, -1e9  # not 0, 최솟값&최댓값
for k, v in n_dict.items():
    if v == max_val:
        mode = k
        cnt += 1
        if cnt == 2:
            break
    #mini = min(mini, k)
    #maxi = max(maxi, k)

print(mode)
print(max(n_list)-min(n_list))