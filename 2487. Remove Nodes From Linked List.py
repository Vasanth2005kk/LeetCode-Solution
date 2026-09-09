from typing import Optional
from linkedlistfunc import createNode, LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        Data = []
        curr = head
        while curr:
            Data.append(curr.val)
            curr = curr.next

        max_value = 0
        result = []

        for i in range(len(Data) - 1, -1, -1):
            if Data[i] >= max_value:
                result.append(Data[i])
                max_value = Data[i]

        result.reverse()

        curr = head

        for value in result:
            curr.val = value
            curr = curr.next

        if curr:
            prev = head
            while prev.next != curr:
                prev = prev.next
            prev.next = None

        return head


head = [5,2,13,3,8]
head =  createNode(head)
obj = Solution().removeNodes(head)