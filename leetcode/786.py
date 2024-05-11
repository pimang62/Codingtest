'''
[K-th Smallest Prime Fraction]
sorted integer array `arr`,
`1` and "prime" numbers

0 <= i < j < arr.length
arr[i] / arr[j]

Return the `kth` smallest fraction
2 <= arr.length <= 1000
'''
from typing import List
from heapq import heappush

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        
        q = []  # (1/5, 1, 5)
        for i in range(N):
            for j in range(i+1, N):
                # heappush(q, (arr[i]/arr[j], arr[i], arr[j]))
                q.append((arr[i]/arr[j], arr[i], arr[j]))
        
        # for _ in range(k):
        #     _, a, b = heappop(q)
        q.sort(key=lambda x: x[0])

        _, a, b = q[k-1]
        return [a, b]

