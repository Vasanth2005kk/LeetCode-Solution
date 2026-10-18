from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        Value = []
        curr = head
        while curr:
            Value.append(curr.val)
            curr =  curr.next

        output = []
        length = len(Value)
        
        for index in range(length):
            if index % 2 == 0:
                output.append(Value[index//2])
            else:
                output.append(Value[length - 1 - index//2])

        temp =  head
        index = 0
        while temp:
            temp.val = output[index]
            index +=1
            temp =  temp.next

        return head
    
head =  [1,2,3,4]
head = [1,2,3,4,5]
head = createNode(head)

obj = Solution().reorderList(head)
print(obj)

# Output: [1,4,2,3]