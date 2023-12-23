# "non-empty" array A consisting of N
# (P, Q), 0 ≤ P ≤ Q < N, slice of array A
# sum of a slice (P, Q), A[P] + A[P+1] + ... + A[Q]. : [P, Q]
# returns the "maximum sum" of any slice of A.
import sys

# 0% : ... , 100% : O(N)
def solution(A):
    N = len(A)  # [1..1000000]
    tmp = 0
    answer = -sys.maxsize
    for i in range(N):
        answer = max(answer, tmp+A[i])
        tmp = max(0, tmp+A[i])  # 더한 값이 음수가 나오면 이전 값을 0으로 만들어 줌!
    return answer

print(solution(A=[3, 2, -6, 4, 0]))
print(solution(A=[3, 2, -6, 8, 0]))  # 3+2-6+8 : 아무리 더해줘봤자 -가 등장했던 순간이 지나면 없애고 새로 시작하는 게 이득임!!
print(solution(A=[3, 2, -6, 13, 0])) # -1+13 < 13 !!