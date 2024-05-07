'''
[Remove Nodes From Linked List]
given the `head`
every node which has a node with a "greater" value,  "right" side of it.

Return the head of the modified
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        stack = []
        while now:
            while stack and stack[-1].val < now.val:
                stack.pop()
            stack.append(now)  # now.val, now.next
            now = now.next
        
        ln = ListNode(val=0, next=None)
        prev = ln  # 0 - next
        for node in stack:
            prev.next = node  # 0 - 13
            prev = prev.next  # 13 - next
        
        prev.next = None  # 0 - 13 - 8 - None 연결

        return ln.next


