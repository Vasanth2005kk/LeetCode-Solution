from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        curr = head
        check = []
        lastValue = 0
        while curr.next:
            GcdValue = self.findGCD(curr.val,curr.next.val)
            check.append(curr.val)
            check.append(GcdValue)
            lastValue = curr.next.val
            # print(curr.val,curr.next.val,"==> ",GcdValue)
            curr = curr.next
        if lastValue != 0:
            check.append(lastValue)
        # print(check)

        head = ListNode(check[0])
        curr = head
        for i in range(1,len(check)):
            node = ListNode(check[i])
            curr.next = node
            curr = curr.next

        return head
            
    def findGCD(self,a, b):
        if b == 0:
            return a
        return self.findGCD(b, a % b)

head = [18,6,10,3]

head = createNode(head)
obj = Solution().insertGreatestCommonDivisors(head)
LinkedListPrint(obj)