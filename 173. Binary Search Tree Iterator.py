from BinarySearchTreefunc import create_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.values = []
        self.rootValues(root, self.values)
        self.index = -1

    def rootValues(self, root, values):
        if not root:
            return

        self.rootValues(root.left, values)
        values.append(root.val)
        self.rootValues(root.right, values)

    def next(self) -> int:
        self.index += 1
        return self.values[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.values) - 1


# Your BSTIterator object will be instantiated and called as such:
root = [7, 3, 15, None, None, 9, 20]
root = create_tree(root)
bSTIterator = BSTIterator(root)

print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False