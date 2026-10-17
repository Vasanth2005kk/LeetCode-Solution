from BinarySearchTreefunc import create_tree , inorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return 
        
        # root.left , root.right =  root.right , root.left

        return root

root = [2,1,3]
root =  create_tree(root)

obj = Solution().invertTree(root)
print(obj)


print("InOrder : ",inorder(obj))
