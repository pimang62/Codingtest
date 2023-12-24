'''
[최솟값 찾기] 모토톤 큐

A = [A_1, A_2, ..., A_N]

D_i = A_i-L+1 ~ A_i : window sizs L
각 배열의 최솟값?
'''
from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

q = deque()
d = [0]*N

# idx 없이 window size만 가지고 해서는 안됨!
for i in range(N):
    # 첫 인덱스가 i-L보다 작은 원소라면 : while -> if ok
    while q and q[0][0] <= i-L:  # i일 때 window안의 첫 인덱스는 i-L+1임
        q.popleft()  # 원소 하나 빼기
    while q and q[-1][1] >= A[i]:  # 이전에 저장된 값(3, 5)이 나(2)보다 크다면
        q.pop()  # 맨 뒤 원소 빼기(3, ) -> ( )
    q.append((i, A[i]))  # (2)
    d[i] = q[0][1]  # 맨 앞 원소가 내 구간 안의 가장 작은 수!!
    
print(*d)