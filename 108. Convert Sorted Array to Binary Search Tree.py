from typing import List
from BinarySearchTreefunc import inorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums):
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, left, right):

        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = self.build(nums, left, mid - 1)

        root.right = self.build(nums, mid + 1, right)

        return root

nums = [-10,-3,0,1,5,9]
obj = Solution().sortedArrayToBST(nums)

inorder(obj)