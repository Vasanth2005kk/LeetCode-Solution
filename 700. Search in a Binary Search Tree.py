from BinarySearchTreefunc import create_tree , inorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return root
        
        if root.val ==  val:
            return root
        elif root.val > val:
            tree = self.searchBST(root.left,val)
        else:
            tree = self.searchBST(root.right,val)
            
        return tree



root = [4,2,7,1,3]
val = 2

root =  create_tree(root)

obj = Solution().searchBST(root,val)
print(obj)

print("In Order :",inorder(obj))