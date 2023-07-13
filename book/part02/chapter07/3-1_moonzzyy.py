# 떡볶이 떡 만들기
# 적어도 M만큼의 떡을 가져가기 위해 높이의 최대값
# bisect 모듈 활용 O(MN)

import bisect
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))

count = [] # 자른 길이에 따른 잘린 떡의 길이
for i in range(max(arr)-1,-1,-1):
    temp = 0  # 잘린 떡의 합
    for n in arr:
        if n > i: temp += n - i
    count.append(temp)
print(max(arr)-bisect.bisect_left(count, M))