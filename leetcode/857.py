'''
[Minimum Cost to Hire K Workers]
`n` workers, `quality` and `wage`
hire exactly `k` workers

1. paid at "least" their minimum wage
2. must be directly "proportional" to their quality

return the "least" amount of money
1 <= k <= n <= 10**4
'''
from typing import List
from heapq import heappush, heappop, heapify

# Version 1
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([(w/q, q) for w, q in zip(wage, quality)])  # ratio, quality
        
        q = []
        qual_sum = 0  # initial cheap quality sum
        max_rate = 0  # initial max rate in k
        
        for i in range(k):
            rate, qual = ratio[i]
            max_rate = max(max_rate, rate)  # max ratio
            qual_sum += qual  # quality sum
            heappush(q, (-qual))  # max heap
        
        cost = qual_sum * max_rate

        for i in range(k, len(quality)):
            rate, qual = ratio[i]
            max_rate = max(max_rate, rate)
            qual_sum += heappop(q) + qual  # k내의 큰 quality 빼고 현재 quality 추가
            heappush(q, (-qual))
            cost = min(cost, qual_sum * max_rate)

        return cost

# Version 2
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([(w/q, q) for w, q in zip(wage, quality)])  # ratio, quality
        answer = 1e9

        q = []
        qual_sum = 0
        for rate, qual in ratio:
            qual_sum += qual
            heappush(q, -qual)

            if len(q) > k:  # 뽑아서 +(-val)
                qual_sum += heappop(q)
            if len(q) == k:  # 다시 비교
                answer = min(answer, qual_sum * rate)

        return answer