from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find cycle entry
                fast = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        # No cycle
        return None

head = [3,2,0,-4]
pos = 1

head = createNode(head)

obj = Solution().detectCycle(head)
LinkedListPrint(obj)