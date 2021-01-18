"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linked_list import LinkedList

# The examples I want to test are
# "a, b, c; -1" -> None 
# "a, b, c; 3" -> None 
# "a, b, c; 0" -> c 
# "a, b, c; 2" -> a 
# "a, b, c; 1" -> b 
def kth_to_last(self, k: int):
    l = len(self)
    if k < 0 or k >= l:
        return None
    node = self.head
    count, final = 0, l - k - 1
    while count != final:
        count += 1
        node = node.next
    return node

LinkedList.kth_to_last = kth_to_last

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        ll, k = line.strip().split("; ")
        k = int(k)
        ll = LinkedList(ll.split(", "))
        result = ll.kth_to_last(k)
        if result:
            print(result.value)
        else:
            print("Invalid k")

