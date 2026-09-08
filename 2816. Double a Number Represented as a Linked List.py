from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def double(node):
            if node is None:
                return 0

            carry = double(node.next)

            value = node.val * 2 + carry

            node.val = value % 10

            return value // 10

        carry = double(head)

        if carry:
            newNode = ListNode(carry)
            newNode.next = head
            head = newNode

        return head




head = [1,2,3]
head =  createNode(head)
obj = Solution().doubleIt(head)
LinkedListPrint(obj)