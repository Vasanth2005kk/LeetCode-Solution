class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # HashMap
        self.store = {}

        # Dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    # Add node just after head
    def addNode(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    # Remove node
    def removeNode(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:

        if key not in self.store:

            print("get :", -1)
            return -1

        node = self.store[key]

        # Move node to front
        self.removeNode(node)
        self.addNode(node)

        print("get :", node.value)

        return node.value


    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.store:

            node = self.store[key]

            # Remove old node
            self.removeNode(node)

            # Update value
            node.value = value

            # Move to front
            self.addNode(node)

        else:

            # Create new node
            node = Node(key, value)

            # Store in HashMap
            self.store[key] = node

            # Add to front
            self.addNode(node)


        # Capacity exceeded
        if len(self.store) > self.capacity:

            # Least recently used node
            lru = self.tail.prev

            # Remove from linked list
            self.removeNode(lru)

            # Remove from HashMap
            del self.store[lru.key]


        # print("put :", [(k, v.value) for k, v in self.store.items()])


obj = LRUCache(2)

obj.get(2)
obj.put(2, 6)
obj.get(1)
obj.put(1, 5)
obj.put(1, 2)
obj.get(1)
obj.get(2)

'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = []

    def get(self, key: int) -> int:

        for index, value in enumerate(self.store):

            if value[0] == key:

                # Remove old position
                self.store.pop(index)

                # Move to front
                self.store.insert(0, value)

                # print("get :", value[1])
                # print("store :", self.store)

                return value[1]

        # print("get :", -1)
        # print("store :", self.store)

        return -1

    def put(self, key: int, value: int) -> None:

        # If key already exists
        for index, item in enumerate(self.store):

            if item[0] == key:

                # Remove old position
                self.store.pop(index)

                # Add updated value to front
                self.store.insert(0, [key, value])

                # print("put :", self.store)
                return

        # New key
        self.store.insert(0, [key, value])

        # Remove least recently used
        if len(self.store) > self.capacity:
            self.store.pop()

        # print("put :", self.store)

'''