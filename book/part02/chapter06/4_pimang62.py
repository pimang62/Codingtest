n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# k만큼 반복
for i in range(k):
    # A의 원소 중 가장 작은 수 인덱스 추출
    A_idx = A.index(min(A))
    # B의 원소 중 가장 큰 수 인덱스 추출
    B_idx = B.index(max(B))
    # A의 가장 작은 수와 B의 가장 큰 수 swap
    A[A_idx], B[B_idx] = B[B_idx], A[A_idx]

print(sum(A))