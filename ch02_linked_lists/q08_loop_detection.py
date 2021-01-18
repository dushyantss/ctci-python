"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C[the same C as earlier]
Output: C
"""
"""
My scratchpad
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> ?

1) ? is at 1
so, the steps are
p1  p2
1   1
2   3
3   5
4   7
5   9
6   2
7   4
8   6
9   8
1   1

2) ? is at 2
p1  p2
1   1
2   3
3   5
4   7
5   9
6   3
7   5
8   7
9   9
2   3
3   5
4   7
5   9
6   3
7   5
8   7
9   9

3) ? is at 3
p1  p2
1   1
2   3
3   5
4   7
5   9
6   4
7   6
8   8
9   3
3   5
4   7
5   9
6   4
7   6
8   8

4) ? is at 4
p1  p2
1   1
2   3
3   5
4   7
5   9
6   5
7   7

5) ? is at 5
p1  p2
1   1
2   3
3   5
4   7
5   9
6   6

6) ? is at 6
p1  p2
1   1
2   3
3   5
4   7
5   9
6   7
7   9
8   7
9   9

7) ? is 7
p1  p2
1   1
2   3
3   5
4   7
5   9
6   8
7   7

8) ? is 8
p1  p2
1   1
2   3
3   5
4   7
5   9
6   9
7   9
8   9
9   9

9) ? is 9
p1  p2
1   1
2   3
3   5
4   7
5   9
6   9
7   9
8   9
9   9

Suppose slow runner has to take k steps to reach the start of the loop. In the same time fast has traversed 2k steps.
Suppose length of loop is l.
When slow reaches i = 0 of loop, fast is at (2k(steps traversed by fast) - k(distance of loop start from list start)) mod l(the length of loop, which can be smaller than k and thus, the final index of fast will not be k, but a modulus value)

Thus, distance between them is l - (k mod l). For each step slow takes, fast takes 2 steps, so we reduce the distance between them by 1 for each step taken. Thus, it'll take them k(distance of loop start from list start) + l - (k mod l) steps to intersect.
Now, from the point of intersection, if we look within the loop, the two pointers are k mod l steps away from the start of the loop. We can also say that they are k steps away from the loop(which is bigger than k mod l, but is also a point in time when they'll intersect. And we know that the start of the loop is k steps from the start of the list. So, if we move a pointer from the list start and the intersection point at the speed of 1 step each, they'll collide at the intersection.
"""
from linked_list import SinglyLinkedList

def detect_loop_v1(self):
    nodes = set()
    for node in self:
        if node in nodes:
            return node
        else:
            nodes.add(node)

    return None

def detect_loop(self):
    if not self.head:
        return None

    slow, fast = self.head, self.head

    slow, fast = slow.next, fast.next.next
    while slow != fast:
        slow, fast = slow.next, fast.next.next

    # Now that we have the intersection, we start two pointers, 
    # one from head and one from intersection and where they collid is where the loop begins.
    node = self.head
    while node != slow:
        node, slow = node.next, slow.next

    return node

SinglyLinkedList.detect_loop = detect_loop

if __name__ == "__main__":
    ll = SinglyLinkedList([1,2,3,4,5,6])
    node2 = ll.head.next
    node6 = node2.next.next.next.next
    node6.next = node2
    print(ll.detect_loop().value)

