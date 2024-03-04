'''
[반도체 설계]

n개의 포트가 다른 n개의 포츠와 어떻게 연결?
연결선이 서로 겹치지 않으면서 최대 몇 개?

6
4 2 6 3 1 5

>>> 2 3 5 : 3

최장 증가 부분 수열 : LIS
1. DP
2. Binary Search
'''
n = int(input())
nlist = list(map(int, input().split()))

# 1. DP : O(N^2)
d = [1]*n

for i in range(1, n):  # 1부터 하나씩 움직이면서
    for j in range(0, i):  # 앞에걸 본다
        if nlist[j] < nlist[i]:
            d[i] = max(d[i], d[j]+1)  # 이전 최장 개수 + 1

print(max(d))

# 2. Binary Search : O(NlogN)
def binary_search(L, target):
    start, end = 0, len(L)
    while start <= end:
        mid = (start+end) // 2
        if L[mid] < target:
            start = mid + 1
        else:
            # end-1가 start 
            end = mid - 1
    return start

L = [nlist[0]]  # LIS list

for i in range(1, n):
    if L[-1] < nlist[i]:  # 더 큰 수라면 그냥 넣기
        L.append(nlist[i])
    else:
        idx = binary_search(L, nlist[i])  # L 배열에 집어넣을 인덱스 찾아오기
        L[idx] = nlist[i]

print(len(L))