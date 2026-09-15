from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        curr1 = list1
        count = 0
        splite = None
        while curr1.next:
            count+=1
            if count == a:
                for i in range(a,b+1):
                    if curr1.next:
                        curr1.next = curr1.next.next
                splite = curr1.next
                curr1.next = list2
            curr1 = curr1.next
        curr1.next = splite

        return list1

list1 = [10,1,13,6,9,5]
list1 = createNode(list1)
a = 3
b = 4
list2 = [1000000,1000001,1000002]
list2 = createNode(list2)

obj = Solution().mergeInBetween(list1,a,b,list2)
LinkedListPrint(obj)