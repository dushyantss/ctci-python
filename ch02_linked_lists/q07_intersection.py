"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value.That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""
from linked_list import SinglyLinkedList

def has_intersection_v1(self, ll2):
    if not ll2 or not ll2.head:
        return None

    for node in self:
        for node2 in ll2:
            if node == node2:
                return node

    return None

def has_intersection_v2(self, ll2):
    if not ll2 or not ll2.head:
        return None
    nodes = set(self)
    for node in ll2:
        if node in nodes:
            return node

    return None

def has_intersection(self, ll2):
    if not self.head or not ll2 or not ll2.head:
        return None
    # If intersection happens, then that means the last element is the same
    # Better yet, if we draw the lists on paper and align their tails to the same x coordinate
    # Then we just need to move the pointers forward till we find the same node
    # i.e. 1 -> 2 -> 3 -> 4
    #           5 -> 3 -> 4
    len1, len2 = len(self), len(ll2)
    node1, node2 = self.head, ll2.head
    if len1 > len2:
        for i in range(len1 - len2):
            node1 = node1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            node2 = node2.next

    while node1 is not node2:
        node1, node2 = node1.next, node2.next
    
    return node1


SinglyLinkedList.has_intersection = has_intersection

if __name__ == "__main__":
    ll1 = SinglyLinkedList([1,2,3])
    ll2 = SinglyLinkedList()
    ll2.head = ll1.head.next.next
    print(ll1.has_intersection(ll2).value)
    ll3 = SinglyLinkedList([1,2])
    print(ll1.has_intersection(ll3))
    ll4 = None
    print(ll1.has_intersection(ll4))
    ll5 = SinglyLinkedList()
    print(ll1.has_intersection(ll5))


