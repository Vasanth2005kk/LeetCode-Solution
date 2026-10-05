from BinarySearchTreefunc import create_tree , inorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        value = []
        self.inorder(root,value)

        return root

    def inorder(self,root,value):
        if root is None:
            return

        self.inorder(root.right,value)
        value.append(root.val)
        # print(root.val,value)
        root.val = sum(value)
        self.inorder(root.left,value)



root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = create_tree(root)

obj = Solution().bstToGst(root)
print(obj)


print("InOrder : ")
inorder(obj)