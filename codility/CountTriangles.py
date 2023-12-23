# triplet (P, Q, R) triangular, 0 ≤ P < Q < R < N
# A[P] + A[Q] > A[R]
# return 4, the "number" of triangular triplets in this array.
# 효율성 72%, 정확성 100% : O(N**3)

def solution(A):
    A.sort()
    N = len(A)
    answer = 0
    for x in range(N-2):
        for y in range(x+1, N-1):
            z = y+1
            while z < N and (A[x]+A[y] > A[z]):
                # print(x, y, z)
                z += 1
            answer += z-(y+1)
    return answer

# 100% : O(N**2)
def solution(A):
    N = len(A)
    # [1, 2, 5, 8, 10, 12]
    A.sort()

    cnt = 0  # 모든 경우의 수
    for x in range(N-2):
        z = x+2  # !!
        for y in range(x+1, N-1):
            while z < N and (A[x]+A[y] > A[z]):
                z += 1
            cnt += z-(y+1)
    return cnt