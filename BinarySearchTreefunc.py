class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def create_tree(root):
    if not root:
        return None

    nodes = []

    # Create all nodes
    for value in root:
        if value is None:
            nodes.append(None)
        else:
            nodes.append(Node(value))

    # Connect left and right children
    for i in range(len(nodes)):
        if nodes[i] is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]

        if right < len(nodes):
            nodes[i].right = nodes[right]

    return nodes[0]


# Inorder: Left -> Root -> Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


if __name__ == "__main__":
    # Input
    root = [10, 5, 15, 3, 7, None, 18]

    # Create tree
    tree = create_tree(root)

    # Traversals
    print("Inorder:")
    inorder(tree)

    print("\nPreorder:")
    preorder(tree)

    print("\nPostorder:")
    postorder(tree)