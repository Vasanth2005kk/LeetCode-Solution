from typing import Optional
from linkedlistfunc import createNode,LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Length = 0
        current = head
        while current:
            Length+=1
            current = current.next

        if Length == n:
            return head.next

        Length =  Length-n
        count = 0
        current = head

        while current:
            count +=1
            if count == Length:
                current.next =  current.next.next
                break
            current = current.next
        
        return head


head = [1, 2, 3, 4, 5]
n = 2

head =  createNode(head)
obj = Solution().removeNthFromEnd(head,n)
