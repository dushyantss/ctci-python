"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from linked_list import SinglyLinkedList

def partition(self, value):
    """
    We'll create two temp lists one for each side of partition, and at the end we merge them.
    To implement, we can work in place, we will need 4 pointers, one each to mark head/tail beginning
    and one each to mark the current node for head/tail.
    """
    head, tail, hnode, tnode = None, None, None, None
    for node in self:
        if node.value < value:
            if not head:
                head = node
                hnode = node
            else:
                hnode.next = node
                hnode = node
        else:
            if not tail:
                tail = node
                tnode = node
            else:
                tnode.next = node
                tnode = node
    # Now we clean up the nexts of the last elements of head and tail
    if not head:
        # in this case, tail is all there is
        self.head = tail
    else:
        self.head = head
        hnode.next = tail
        if tnode:
            tnode.next = None


SinglyLinkedList.partition = partition

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        ll, n = line.strip().split("; ")
        ll = SinglyLinkedList((int(val) for val in ll.split(", ")))
        n = int(n)
        ll.partition(n)
        for node in ll:
            print(node.value)

