from BinarySearchTreefunc import create_tree , preorder


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if root is None:
            return

        root_left = root.left
        root_right = root.right

        self.flatten(root_left)
        self.flatten(root_right)

        root.left = None
        root.right = root_left

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = root_right


root = [1,2,5,3,4,None,6]

root = create_tree(root)

obj = Solution().flatten(root)

preorder(root)