"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo­
rithm to create a binary search tree with minimal height.
"""
from binary_tree import BinaryNode, in_order, pre_order, post_order

def minimal_tree(arr):
    if not arr:
        return None
    return do_minimal_tree(arr, 0, len(arr) - 1)

def do_minimal_tree(arr, low, high):
    if low > high:
        return None
    mid = (low + high) // 2

    node = BinaryNode(arr[mid])
    node.left = do_minimal_tree(arr, low, mid - 1)
    node.right = do_minimal_tree(arr, mid + 1, high)

    return node

if __name__ == '__main__':
    tree = minimal_tree([1,2,3,4,5,6,7,8,9,10])
    in_order(tree, lambda n: print(n.value))
    print('')
    pre_order(tree, lambda n: print(n.value))
    print('')
    post_order(tree, lambda n: print(n.value))

