from linkedlistfunc import createNode, LinkedListPrint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head:
            while head.val == val and head.next is not None:
                head = head.next
            if head.val == val and head.next is None:
                return 
            
            temp = head
            
            while temp.next:
                if temp.next.val == val:
                    temp.next =  temp.next.next
                    continue
                temp = temp.next
            
            return head
        return

head = [7,7,7,7]
val = 7
head =  createNode(head)

obj = Solution().removeElements(head,val)

LinkedListPrint(obj)