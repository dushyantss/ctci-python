"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
from linked_list import LinkedList, Node

def remove_dups(self):
    vals = set()
    for node in self:
        if node.value in vals:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        else:
            vals.add(node.value)

def remove_dups_no_buffer(self):
    for node in self:
        other = node.next
        while other != None:
            if other.value == node.value:
                other.prev.next = other.next
                if other.next:
                    other.next.prev = other.prev
            other = other.next

LinkedList.remove_dups = remove_dups_no_buffer

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        vals = line.strip().split(", ")
        ll = LinkedList(vals)
        ll.remove_dups()
        for node in ll:
            print(node.value)

