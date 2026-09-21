from typing import List, Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        pass


m = 3
n = 5
head = createNode([3,0,2,6,8,1,7,9,4,2,5,5,0])
obj = Solution().spiralMatrix(m, n, head)