"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.
"""
from q02_minimal_tree import minimal_tree

def successor(node):
    """
    Successor is the next highest value.

    In a bst, every value in the left tree is smaller than the node and every value in the right is greater.
              8
        4           13
      2   6     10      16
    1  3 5  7 9   11  15  18
    """
    if not node:
        return None

    if node.right:
        result = node.right
        while result.left:
            result = result.left
        return result.value

    while node.parent:
        if node == node.parent.left:
            return node.parent.value
        node = node.parent

    return None

if __name__ == '__main__':
    tree = minimal_tree([1,2,3,4,5,6,7,8,16,38,123])
    print(tree.value, successor(tree))
    print(tree.right.right.value, successor(tree.right.right))
    print(tree.right.right.right.value, successor(tree.right.right.right))
    print(tree.left.left.value, successor(tree.left.left))

