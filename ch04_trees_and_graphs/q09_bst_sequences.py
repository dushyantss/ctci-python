"""
BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
EXAMPLE
  2
1   3
Input:
Output: {2, 1, 3}, {2, 3, 1}
"""
from collections import deque

def bst_sequences(node):
    result = []
    if not node:
        result.append(deque())
        return result

    prefix = deque()
    prefix.append(node.value)
    left_seq = bst_sequences(node.left)
    right_seq = bst_sequences(node.right)

    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave(left, right, weaved, prefix)
            result += weaved

    return result

def weave(first, second, results, prefix):
    if not first or not second:
        result = prefix.copy()
        result += first
        result += second
        results.append(result)
        return

    first_head = first.popleft()
    prefix.append(first_head)
    weave(first, second, results, prefix)
    prefix.pop()
    first.appendleft(first_head)

    second_head = second.popleft()
    prefix.append(second_head)
    weave(first, second, results, prefix)
    prefix.pop()
    second.appendleft(second_head)
    

# My solution, for sure more inefficient, but it's mine and it's very simple conceptually
def bst_sequences_v1(picks, results):
    # At each step, we have a list of possible slots that can be filled
    # Whenever we visit a node, we open two more possible slots, its left or right values
    if not picks:
        return results
    result = []
    for p in picks:
        # For each possible pick(e.g. slot which can be filled)
        # We create a new possible set of picks after filling this particular slot
        # And adding its children if possible.
        new_picks = [np for np in picks if np != p]
        if p.left:
            new_picks.append(p.left)
        if p.right:
            new_picks.append(p.right)
        # Now, we need to append this result to all the combinations which resulted in
        # this particular pick to be selected.
        new_results = [[val for val in arr] for arr in results]
        if not new_results:
            new_results.append([p.value])
        else:
            for arr in new_results:
                arr.append(p.value)
        result += bst_sequences(new_picks, new_results)

    return result

if __name__ == '__main__':
    from q02_minimal_tree import minimal_tree
    tree = minimal_tree([1,2,3,4,5])

    print(bst_sequences(tree))

