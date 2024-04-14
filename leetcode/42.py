'''
[Trapping Rain Water]
Given n non-negative integers
where the "width" of each bar is "1"
"how much" water it can trap after raining.

0 <= height[i] <= 10**5

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        highest_index = height.index(max(height))
        
        answer = 0
        h_stack = [-1]
        for i in range(0, highest_index):
            if h_stack[-1] < height[i]:  # update
                h_stack.append(height[i])
            answer += (h_stack[-1]-height[i])  # add substract

        h_stack = [-1]
        for j in range(len(height)-1, highest_index, -1):
            if h_stack[-1] < height[j]:
                h_stack.append(height[j])
            answer += (h_stack[-1]-height[j])
        
        return answer
