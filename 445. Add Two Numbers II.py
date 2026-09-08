from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        Add1 = ""
        Add2 = ""

        curr1 = l1
        while curr1:
            Add1 += str(curr1.val)
            curr1 = curr1.next
        curr2 = l2
        while curr2:
            Add2 += str(curr2.val)
            curr2 = curr2.next

        output = str(int(Add1) + int(Add2))
        if len(Add1) > len(Add2):
            head = l1
        else:
            head = l2

        # LinkedListPrint(head)

        head = ListNode(int(output[0]))
        curr = head
        for i in range(1,len(output)):
            node = ListNode(int(output[i]))
            curr.next = node
            curr = curr.next

        return head

l1 = [5]
l2 = [5]

l1 = createNode(l1)
l2 = createNode(l2)

obj = Solution().addTwoNumbers(l1,l2)
LinkedListPrint(obj)