'''
[Sum of Left Leaves]
Given the root of a binary tree.
return the sum of all "left" leaves.

A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 24
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:  # leaf!
                if is_left:
                    return node.val  # leftself
                else:
                    return 0
            left_sum = dfs(node.left, True)
            right_sum = dfs(node.right, False)
            return left_sum + right_sum
        
        return dfs(root, False)

## BFS
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, False)])  # node, is_left
        total = 0

        while q:
            node, is_left = q.popleft()

            if is_left and not node.left and not node.right:
                total += node.val
            
            if node.left:
                q.append((node.left, True))
            if node.right:  # exclude null 
                q.append((node.right, False))
        
        return total