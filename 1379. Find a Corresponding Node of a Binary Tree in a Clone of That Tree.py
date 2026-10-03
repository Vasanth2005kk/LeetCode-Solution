from BinarySearchTreefunc import create_tree , inorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = self.travals(cloned, target)
        return ans

    def travals(self, root, target):
        if root is None:
            return None

        # Search left
        ans = self.travals(root.left, target)

        if ans:
            return ans

        # Check current node
        if root.val == target.val:
            return root

        # Search right
        ans = self.travals(root.right, target)

        if ans:
            return ans

        return None


tree = [7,4,3,None,None,6,19]
target = 3

tree = create_tree(tree)
target = create_tree([target])

obj = Solution().getTargetCopy(tree, tree, target)
print(obj)

print("inorder of original tree : ", inorder(tree))