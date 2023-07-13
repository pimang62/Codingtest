# 떡볶이 떡 만들기 (어려움)
# 적어도 M만큼의 떡을 가져가기 위해 높이의 최대값
# 이진 탐색 구현
# 반복문을 통해 현재 떡의 합을 구하고 target과 비교
# target보다 작으면 더 잘라야 하고 반대면 덜 잘라야 함
# 이진탐색할 때, O(NlogM)?
# 같은 문제: https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def solve(x):
    temp = 0  # 잘린 떡의 합
    for n in arr:
        if n>x: temp += n - x
    return temp>=M

N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, max(arr)
while s < e:
    mid = (s+e+1) // 2
    if solve(mid): s=mid
    else: e=mid-1
print(s)