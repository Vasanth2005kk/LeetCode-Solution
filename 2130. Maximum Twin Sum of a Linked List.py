from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        data = []
        curr = head
        while curr:
            n+=1
            data.append(curr.val)
            curr = curr.next
            
        maxValue = 0
        for i in range(n):
            if 0 <= i <= (n / 2) - 1:
                total = data[i]+data[n-1-i]
                if maxValue <= total :
                    maxValue = total

        return maxValue


head = [5,4,2,1]
head= createNode(head)

obj = Solution()
print(obj.pairSum(head))