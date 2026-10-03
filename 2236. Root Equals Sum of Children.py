from BinarySearchTreefunc import create_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        rootValue =  root.val
        leftValue = root.left.val
        rightValue = root.right.val

        if rootValue == leftValue + rightValue:
            return True
        
        return False

root = [10,4,6]
root = create_tree(root)

obj = Solution().checkTree(root)
print(obj)