from linkedlistfunc import createNode, LinkedListPrint
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =  head
        findcount = 0
        while temp:
            findcount +=1
            Prev = temp.val
            if findcount % 2 == 1 and temp.next != None:
                Emty = temp.next.val    
                temp.next.val = Prev
                temp.val = Emty
                
            temp =  temp.next
        
        return head


head = [1,2,3,4]

head =  createNode(head)
obj  =  Solution().swapPairs(head)

LinkedListPrint(obj)