from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return None
        
        Values = []

        temp = head
        while temp:
            Values.append(temp.val)   
            temp =  temp.next
        
        length = len(Values)-1
        for i in range(length+1):
            if Values[i] != Values[length-i]:
                return False
        return True 

head = [1,2,1]
head =  createNode(head)

obj = Solution().isPalindrome(head)
print(obj)
