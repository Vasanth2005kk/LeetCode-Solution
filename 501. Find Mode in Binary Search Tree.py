from BinarySearchTreefunc import create_tree , inorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        data = {}
        self.travel(root, data)

        if not data:
            return []

        maxValue = max(data.values())

        return [key for key, count in data.items() if count == maxValue]

    def travel(self, root, data):
        if root is None:
            return

        self.travel(root.left, data)

        data[root.val] = data.get(root.val, 0) + 1

        self.travel(root.right, data)

root = [1,None,2,2]

root = create_tree(root)

inorder(root)

obj = Solution().findMode(root)

print(obj)