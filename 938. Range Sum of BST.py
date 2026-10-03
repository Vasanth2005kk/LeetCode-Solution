from BinarySearchTreefunc import create_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        result = []
        self.travels(root,result,low,high)

        return sum(result)


    def travels(self,root,result,low,high):
        if root is None:
            return

        self.travels(root.left,result,low,high)
        
        if low <= root.val and high >= root.val:
            result.append(root.val)
            # print(f"value :{root.val} low :{low} high : {high} result : {result}")
        
        self.travels(root.right,result,low,high)







root = [10,5,15,3,7,None,18]
low = 7
high = 15

root = create_tree(root)


obj = Solution().rangeSumBST(root,low,high)
print(obj)
