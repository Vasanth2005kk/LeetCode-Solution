from BinarySearchTreefunc import create_tree , preorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        data= []
        self.pertreeTravel(root,data)
        return data
    def pertreeTravel(self,root,data):
        if root is None:
            return

        data.append(root.val)
        self.pertreeTravel(root.left,data)
        self.pertreeTravel(root.right,data)


root = [1,None,2,3]
root =  create_tree(root)

obj = Solution().preorderTraversal(root)
print(obj)