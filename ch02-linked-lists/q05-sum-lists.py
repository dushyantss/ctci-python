"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. Output:2 -> 1 -> 9.That is,912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.That is,912.
"""
from linked_list import SinglyLinkedList, SinglyLinkedNode

def inner_step(n1, n2, n3, sum_ll, carry):
    total = carry
    if n1:
        total += n1.value
        n1 = n1.next
    if n2:
        total += n2.value
        n2 = n2.next
    result = total % 10
    carry = total // 10
    new_node = SinglyLinkedNode(result)
    if not n3:
        sum_ll.head = new_node
        n3 = sum_ll.head
    else:
        n3.next = new_node
        n3 = new_node
    return n1, n2, n3, carry

def sum_reverse(self, ll2):
    sum_ll = SinglyLinkedList()
    carry = 0
    n1, n2, n3 = self.head, ll2.head, sum_ll.head
    while n1 and n2:
        n1, n2, n3, carry = inner_step(n1, n2, n3, sum_ll, carry)

    while n1:
        n1, n2, n3, carry = inner_step(n1, n2, n3, sum_ll, carry)

    while n2:
        n1, n2, n3, carry = inner_step(n1, n2, n3, sum_ll, carry)

    if carry:
        n1, n2, n3, carry = inner_step(n1, n2, n3, sum_ll, carry)

    return sum_ll
            
SinglyLinkedList.sum_reverse = sum_reverse

def add_zero_nodes(ll, count):
    node = SinglyLinkedNode(0)
    head = node
    for i in range(count - 1):
        node.next = SinglyLinkedNode(0)
        node = node.next
    node.next = ll.head
    return head

def do_sum_forward(node1, node2):
    if not node1:
        return None, 0
    elif not node1.next:
        total = node1.value + node2.value
        carry = total // 10
        value = total % 10
        return SinglyLinkedNode(value), carry

    child_node, carry = do_sum_forward(node1.next, node2.next)
    total = node1.value + node2.value + carry
    carry = total // 10
    value = total % 10
    node = SinglyLinkedNode(value)
    node.next = child_node
    return node, carry

def sum_forward(self, ll2):
    len1, len2 = len(self), len(ll2)
    if len1 > len2:
        head = add_zero_nodes(ll2, len1 - len2)
        ll2.head = head
        len2 = len1
    elif len2 > len1:
        head = add_zero_nodes(self, len2 - len1)
        self.head = head
        len1 = len2
    if len1 == 0:
        return None
    node, carry = do_sum_forward(self.head, ll2.head)
    if carry > 0:
        head = SinglyLinkedNode(carry)
        node, head.next = head, node

    ll = SinglyLinkedList()
    ll.head = node

    return ll

SinglyLinkedList.sum_forward = sum_forward

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        ll1, ll2 = line.strip().split("; ")
        ll1 = SinglyLinkedList((int(val) for val in ll1.split(', ')))
        ll2 = SinglyLinkedList((int(val) for val in ll2.split(', ')))
        for node in ll1.sum_reverse(ll2):
            print(node.value)
        print("")
        for node in ll1.sum_forward(ll2):
            print(node.value)

