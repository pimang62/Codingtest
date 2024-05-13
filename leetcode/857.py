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

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        