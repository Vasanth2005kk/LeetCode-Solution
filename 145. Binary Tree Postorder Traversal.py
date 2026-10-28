from BinarySearchTreefunc import create_tree , postorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        data = []
        self.postTraversal(root,data)
        print(data)
        return data

    def postTraversal(self,root,data):
        if root is None:
            return

        self.postTraversal(root.left,data)
        self.postTraversal(root.right,data)
        data.append(root.val)




root = [1,None,2,3]

root =  create_tree(root)
obj = Solution().postorderTraversal(root)