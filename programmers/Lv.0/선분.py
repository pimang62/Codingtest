from collections import deque

def solution(lines):
    lines.sort(key=lambda x: x[1])
    ans = [0] * 202
    q = deque(lines)
    while q:
        st, en = q.popleft()     
        for i in range(st, en):
            ans[i+100] += 1
    return ans.count(2) + ans.count(3)
print(solution([[0, 5], [3, 9], [1, 10]]))
print(solution([[0, 2], [-3, -1], [-2, 1]]))