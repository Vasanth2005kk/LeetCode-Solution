from linkedlistfunc import LinkedListPrint,createNode
from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr = []

        # Collect all values
        for head in lists:
            temp = head
            while temp:
                arr.append(temp.val)
                temp = temp.next

        if not arr:
            return None

        arr.sort()

        # Find first non-empty list
        head = None
        for node in lists:
            if node:
                head = node
                break

        # Connect all lists
        prev = None
        for node in lists:
            if not node:
                continue

            if prev:
                prev.next = node

            temp = node
            while temp.next:
                temp = temp.next
            prev = temp

        # Fill sorted values
        temp = head
        i = 0

        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next

        return head
        


# lists = [[1,4,5],[1,3,4],[2,6]]

lists = [createNode([1,4,5]),createNode([1,3,4]),createNode([2,6])]

obj = Solution().mergeKLists(lists)

LinkedListPrint(obj)
