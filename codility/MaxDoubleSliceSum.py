# triplet (X, Y, Z), 0 ≤ X < Y < Z < N, "double" slice.
# A[X + 1] + A[X + 2] + ... + A[Y - 1] + A[Y + 1] + A[Y + 2] + ... + A[Z - 1]
# (0, 3, 6) : [1, 2]+[4, 5]
# (3, 4, 5) : [4, 3]+[5, 4] x
# returns the "maximal" sum of any double slice.
# 중간의 한 칸을 건너 뛰고 왼쪽 오른쪽 최대 찾기!

def solution(A):
    # [3, 2, 6, -1, 4, 5, -1, 2]
    N = len(A)
    l_sum = [0]*N
    r_sum = [0]*N
    for i in range(1, N-1):  # 양 끝 제외!
        l_sum[i] = max(0, A[i], l_sum[i-1]+A[i])
    
    for j in range(N-2, 0, -1):
        r_sum[j] = max(0, A[j], r_sum[j+1]+A[j])

    answer = 0  # -보다 < 0을 가질 수 있으므로!
    for k in range(1, N-1):  # [2, N-3]
        # 한 칸 띄우고
        answer = max(answer, l_sum[k-1] + r_sum[k+1])  
    
    return answer