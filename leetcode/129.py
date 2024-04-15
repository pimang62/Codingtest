'''
[Sum Root to Leaf Numbers]
You are given the root,
containing digits from "0 to 9" only.

1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf
>>> 12 + 13 = 25

'''
from typing import Optional

import sys
sys.set_int_max_str_digits(10000000)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node, path):
            nonlocal answer
            if not node:
                return

            path += str(node.val)
            if not node.left and not node.right:
                answer += int(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, '')

        return answer