from linkedlistfunc import createNode , LinkedListPrint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        arr = []

        temp = list1
        chekcing = True
        while temp:
            arr.append(temp.val)
            if temp.next == None and chekcing:
                temp.next = list2
                chekcing = False
            temp =  temp.next
        arr.sort()

        i = 0
        temp1 = list1
        while temp1:
            temp1.val  =  arr[i]
            i+=1
            temp1 = temp1.next

        return list1

list1 = [1,2,4]
list2 = [1,3,4]

# LinkedListPrint(createNode(list1))
# LinkedListPrint(createNode(list2))

obj = Solution().mergeTwoLists(createNode(list1),createNode(list2))

LinkedListPrint(obj)