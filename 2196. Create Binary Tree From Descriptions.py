from BinarySearchTreefunc import inorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:

        if not descriptions:
            return None

        nodes = {}
        children = set()

        for arr in descriptions:
            parent = arr[0]
            child = arr[1]
            leftOrRight = arr[2]

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            if leftOrRight == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for value in nodes:
            if value not in children:
                return nodes[value]

        return None


descriptions = [
    [20, 15, 1],
    [20, 17, 0],
    [50, 20, 1],
    [50, 80, 0],
    [80, 19, 1]
]

obj = Solution().createBinaryTree(descriptions)

print("inorder traversal:")
inorder(obj)
print()