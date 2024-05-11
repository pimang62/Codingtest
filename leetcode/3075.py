'''
[Maximize Happiness of Selected Children]
given an array happiness of length `n`, + integer `k`
ith child has happiness value `happiness[i]`

you select a child, have not been selected till now "decreases" by 1
cannot become negative

Return the maximum sum
you can achieve by selecting `k` children

1 <= n == happiness.length <= 2 * 10**5
'''
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        t = 0
        answer = 0
        while True:
            if not happiness or (happiness[-1]-t) < 0 or t >= k:
                break
            answer += (happiness.pop()-t)
            t += 1
        return answer
