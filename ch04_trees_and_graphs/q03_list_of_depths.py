"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
from collections import deque
from q02_minimal_tree import minimal_tree

def list_of_depths(node, lists, depth=0):
    if not node:
        return
    lists[depth] = lists.get(depth, deque())
    lists[depth].append(node)
    list_of_depths(node.left, lists, depth + 1)
    list_of_depths(node.right, lists, depth + 1)

if __name__ == '__main__':
    tree = minimal_tree([1,2,3,4,5,6,7,8,9,10])
    lists = {}
    list_of_depths(tree, lists)
    for ll in lists.values():
        for node in ll:
            print(node.value, end=' ')
        print("")

