"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""
from linked_list import SinglyLinkedList

def delete(self, node):
    while node.next.next:
        node.value = node.next.value
        node = node.next
    node.value = node.next.value
    node.next = None

SinglyLinkedList.delete = delete

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        ll, n = line.strip().split("; ")
        ll = SinglyLinkedList(ll.split(", ")) 
        for node in ll:
            if node.value == n:
                ll.delete(node)
                break
        for node in ll:
            print(node.value)

