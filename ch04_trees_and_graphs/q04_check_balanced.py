"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""
from binary_tree import BinaryNode

IMBALANCED = -1

def check_balanced(node):
    if not node:
        return 0
    left_height = check_balanced(node.left)
    if left_height < 0:
        return IMBALANCED

    right_height = check_balanced(node.right)
    if right_height < 0:
        return IMBALANCED

    if abs(left_height - right_height) > 1:
        return IMBALANCED

    return 1 + max(left_height, right_height)

if __name__ == '__main__':
    tree = BinaryNode(0)
    tree.left = BinaryNode(1)
    tree.right = BinaryNode(2)
    # tree.right.left = BinaryNode(6)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(4)
    tree.left.right.right = BinaryNode(5)

    print(check_balanced(tree))
    print(check_balanced(tree.left))

