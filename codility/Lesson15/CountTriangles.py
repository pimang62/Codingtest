# array A consisting of N integers is given
# triplet (P, Q, R) is triangular
# 0 ≤ P < Q < "R" < N, A[P] + A[Q] > A[R]
# returns the "number" of triangular triplets
# return 4

# 70% : with break, 100% : O(N**2)
def solution(A):
    N = len(A)  # [0..1,000]
    if N < 3:  # 0 or 1 or 2
        return 0
    # [1, 2, 5, 8, 10, 12]
    A.sort()
    
    cnt = 0  # 누적합 
    for x in range(N-2):  # [0, N-3]
        z = x+2  # N-1]
        for y in range(x+1, N-1):
            # if z < N and (A[x] + A[y]) <= A[z]:
            #     break  # 한번 걸어줘보기
            while z < N and A[x]+A[y] > A[z]:
                z += 1
            cnt += z-(y+1)
    return cnt