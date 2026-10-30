from BinarySearchTreefunc import create_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        data = []
        self.travelCheck(p, q, data)

        return all(data)

    def travelCheck(self, rootOne, rootTwo, data):

        if rootOne is None and rootTwo is None:
            return

        if rootOne is None or rootTwo is None:
            data.append(False)
            return

        if rootOne.val == rootTwo.val:
            data.append(True)
        else:
            data.append(False)

        self.travelCheck(rootOne.left, rootTwo.left, data)
        self.travelCheck(rootOne.right, rootTwo.right, data)



p = [1,2,3]
q = [1,2,3]

# p = [1,2,1]
# q = [1,1,2]

p = create_tree(p)
q = create_tree(q)

obj = Solution().isSameTree(p,q)
print(obj)