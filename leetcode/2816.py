'''
[Double a Number Represented as a Linked List]
given the `head` of a non-empty
Return the head of the linked list after "doubling"
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
        
        tail = None
        prev = 0  # 곱하다 남아서 더해질 값
        while stack:
            tail = ListNode(0, tail)
            
            prev += stack.pop() * 2  # 9 * 2 = 18
            tail.val = prev % 10  # 8
            prev //= 10  # 1
        
        return tail
            