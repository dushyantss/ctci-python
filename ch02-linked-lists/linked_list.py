class SinglyLinkedNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, iterable=[]):
        self.head = None
        node = None
        for val in iterable:
            if not self.head:
                self.head = SinglyLinkedNode(val)
                node = self.head
            else:
                node.next = SinglyLinkedNode(val)
                node = node.next
        self.tail = node

    def __iter__(self):
        n = self.head
        while n:
            yield n
            n = n.next

    def __len__(self):
        i = 0
        node = self.head
        while node:
            i += 1
            node = node.next
        return i


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

    def __len__(self):
        i = 0
        node = self.head
        while node:
            i += 1
            node = node.next
        return i

