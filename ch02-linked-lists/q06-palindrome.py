"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""
from linked_list import SinglyLinkedList, SinglyLinkedNode

def is_palindrome(self):
    length = len(self)

    stack, i = [], 0
    middle = None
    for node in self:
        if i >= length // 2:
            middle = node
            break
        stack.append(node)
        i += 1
    if length % 2 == 0:
        # We create a fake middle node so that we can compare both values
        node = SinglyLinkedNode(0, middle)
        middle = node

    node = middle
    while node.next:
        if node.next.value != stack.pop().value:
            return False
        node = node.next

    return True


SinglyLinkedList.is_palindrome = is_palindrome

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        ll = SinglyLinkedList(line.strip().split(', '))
        print(ll.is_palindrome())

