from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev =  None
        current =  head

        while current:
            next_node = current.next
            current.next = prev       
            prev = current             
            current = next_node   

        head =  prev     
        return  head
        



head = [1,2,3,4,5]

head = createNode(head)

obj = Solution().reverseList(head)
