'''
[Maximal Rectangle]
Given a rows x cols, binary matrix
find the "largest" rectangle containing only 1
return its "area".

1 <= row, cols <= 200

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
[2, 1, 5, 6, 2, 3, 0]
[0]
[]
'''
# class Solution:  # Time attack
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         n, m = len(matrix), len(matrix[0])

#         def check(x1, y1, x2, y2):
#             return all([
#                 matrix[i][j] == '1'  # str not int
#                 for i in range(x1, x2+1)
#                 for j in range(y1, y2+1)
#             ])  # True or False
        
#         answer = 0
#         for i in range(n):
#             for j in range(m):
#                 for k in range(i, n):
#                     for l in range(j, m):
#                         if check(i, j, k, l):
#                             answer = max(answer, (k-i+1)*(l-j+1))
        
#         return answer

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        if not matrix:
            return 0

        heights = [0] * (m + 1)  # Include an extra element for easier calculation
        max_area = 0
        
        for row in matrix:
            for j in range(m):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            
            # Calculate max area using histogram method
            stack = []  # push index
            for i in range(len(heights)):
                # while if stacked one is bigger than now one
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    h = heights[idx]
                    if not stack:  # from 0 to i
                        w = i
                    else:  # from stack[-1]+1 to i
                        w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area      