from linkedlistfunc import createNode , LinkedListPrint
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        curr = head
        while curr:
            self.nums.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        import random
        value = random.choice(self.nums)
        print(value)
        return value

# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]

# Your Solution object will be instantiated and called as such:
obj = Solution(createNode([1,2,3]))
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
