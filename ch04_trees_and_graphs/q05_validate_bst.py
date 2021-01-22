"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
from math import inf
from binary_tree import BinaryNode

def validate_bst(node, minimum=-inf, maximum=inf):
    if not node:
        return True

    if node.value <= minimum or node.value > maximum:
        return False

    return validate_bst(node.left, minimum, node.value) and validate_bst(node.right, node.value, maximum)

if __name__ == '__main__':
    tree = BinaryNode(0)
    tree.left = BinaryNode(1)
    print(validate_bst(tree))
    print(validate_bst(tree.left))
    tree.left.left = BinaryNode(0)
    tree.left.right = BinaryNode(2)
    tree.left.left.left = BinaryNode(-1)
    print(validate_bst(tree.left))

