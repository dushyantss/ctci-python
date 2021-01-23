"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
"""

def first_common_ancestor(node1, node2, root):
    # First common ancestor means
    # Both come from separate sub trees
    # OR
    # One of them is the ancestor of another
    if node1 is root:
        return node1
    elif node2 is root:
        return node2
    elif not root:
        return None

    is_node1_left = is_descendent(node1, root.left)
    if is_node1_left:
        if is_descendent(node2, root.right):
            return root
        else:
            return first_common_ancestor(node1, node2, root.left)
    else:
        if is_descendent(node2, root.left):
            return root
        else:
            return first_common_ancestor(node1, node2, root.right)

##########################My own solution##########################################
def first_common_ancestor_v1(node1, node2, root):
    # If root is a common ancestor(not necessarily first)
    # Try to check if either left or right is a common ancestor
    # If so, recursively reduce the size of the tree to look in
    # When we finally can't find a common ancestor, we return the result
    node = root

    if not is_common_ancestor(node1, node2, node):
        return None

    result = node

    while node:
        if is_common_ancestor(node1, node2, node.left):
            node = node.left
        elif is_common_ancestor(node1, node2, node.right):
            node = node.right
        else:
            break
        result = node

    return result

def is_common_ancestor(node1, node2, node):
    return is_descendent(node1, node) and is_descendent(node2, node)

def is_descendent(node, root):
    if not root:
        return False

    if node is root:
        return True

    return is_descendent(node, root.left) or is_descendent(node, root.right)

if __name__ == '__main__':
    from q02_minimal_tree import minimal_tree

    tree = minimal_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    node1, node2 = tree.left.left, tree.left.right
    print(tree.value, tree.left.value, node1.value, node2.value)
    print(first_common_ancestor(node1, node2, tree).value)

