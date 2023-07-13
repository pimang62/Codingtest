# 두 배열의 원소 교체
# 배열 A의 모든 원소의 합이 최대가 되도록
# A와 B을 오름차순 정렬하여 K번 바꾸기


import time
import sys
input = sys.stdin.readline
start = time.time()

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
for i in range(K):
    A[i] = B.pop() # 가장 큰 수를 pop

print(sum(A))

end = time.time()
print('\ntime:', end-start)
