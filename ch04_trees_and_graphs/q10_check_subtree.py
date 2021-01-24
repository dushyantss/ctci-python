"""
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.
"""

def check_subtree(t1, t2):
    if not t1 or not t2:
        return False

    if not t1.value == t2.value:
        return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)

    return match_tree(t1, t2)

def match_tree(t1, t2):
    if t1 == t2:
        return True
    if not t1 or not t2 or t1.value != t2.value:
        return False
    
    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)

if __name__ == '__main__':
    from q02_minimal_tree import minimal_tree

    t1 = minimal_tree([1,2,3,5,7,8,9])
    t2 = minimal_tree([1,2,3])
    print(check_subtree(t1, t2))
    t3 = minimal_tree([3,2,1])
    print(check_subtree(t1, t3))

