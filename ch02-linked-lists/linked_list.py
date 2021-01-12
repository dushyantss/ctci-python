class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, iterable=[]):
        self.head = None
        node = None
        for val in iterable:
            if not self.head:
                self.head = Node(val, None, None)
                node = self.head
            else:
                node = Node(val, node, None)
                node.prev.next = node

    def __iter__(self):
        n = self.head
        while n:
            yield n
            n = n.next

