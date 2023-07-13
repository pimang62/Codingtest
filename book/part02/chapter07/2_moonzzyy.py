# 부품 찾기
# 부품이 있으면 yes, 없으면 no
# 이진 탐색 구현
# 반복문을 통해 target보다 큰 경우, 작은 경우, 같은 경우로 나누기
# 정렬할 때 O(NlogN), 이진탐색할 때, O(MlogN)
# 같은 문제: https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

def search(target):
    s, e = 0, N-1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] > target:
            e=mid-1
        elif arr[mid] < target:
            s=mid+1
        else: return 'yes'
    return 'no'

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
arr2 = list(map(int, input().split()))
for target in arr2:
    print(search(target), end=' ')