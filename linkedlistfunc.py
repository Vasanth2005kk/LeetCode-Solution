class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createNode(head):
    firstNode = None
    current = None

    for value in head:
        newNode = ListNode(value)

        if firstNode is None:
            firstNode = newNode
            current = newNode
        else:
            current.next = newNode
            current = newNode
    return  firstNode

def LinkedListPrint(Node):
    while Node:
        print(Node.val, end=" -> ")
        Node = Node.next

    print("None")


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]

    LinkedListPrint(createNode(head))