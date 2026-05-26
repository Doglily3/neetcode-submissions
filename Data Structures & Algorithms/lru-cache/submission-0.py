class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node from linked list
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    # insert node right after head
    def insert(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move to front
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # key already exists
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)

        newNode = Node(key, value)

        self.insert(newNode)
        self.cache[key] = newNode

        # over capacity
        if len(self.cache) > self.cap:

            # least recently used
            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]