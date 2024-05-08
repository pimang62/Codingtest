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
        str_num = ''

        now = head
        while now:
            str_num += str(now.val)
            now = now.next
        
        double_str_num = str(int(str_num) * 2)
        
        ln = ListNode(val=0, next=None)
        prev = ln
        for num in double_str_num:
            prev.next = int(num)
            prev = prev.next
        
        prev.next = None
        return ln.next