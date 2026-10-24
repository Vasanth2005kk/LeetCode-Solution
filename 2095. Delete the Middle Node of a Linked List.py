from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length <= 1:
            return None

        mid = length // 2

        curr = head
        for _ in range(mid - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head


head = [1,2,3,4]

head = createNode(head)
obj = Solution().deleteMiddle(head)

print(obj)