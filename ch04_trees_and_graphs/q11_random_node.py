"""
Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
"""
from random import randint

class BinaryTree:
    def __init__(self):
        self.root = None

    def random(self):
        if not self.root:
            return None

        start = 0
        idx = randint(start, self.root.children_count)
        node = self.root
        while node:
            node_idx = start
            if node.left:
                node_idx += node.left.children_count + 1
            if idx == node_idx:
                return node
            elif idx < node_idx:
                node = node.left
            else:
                node = node.right
                start = node_idx + 1

        return None

if __name__ == '__main__':
    from binary_tree import BinaryNode
    tree = BinaryNode(10)
    tree.children_count = 5
    tree.left = BinaryNode(8)
    tree.left.children_count = 1
    tree.left.right = BinaryNode(9)
    tree.left.right.children_count = 0
    tree.right = BinaryNode(13)
    tree.right.children_count = 2
    tree.right.left = BinaryNode(11)
    tree.right.left.children_count = 0
    tree.right.right = BinaryNode(14)
    tree.right.right.children_count = 0

    bt = BinaryTree()
    bt.root = tree
    randomness_dict = {}
    for i in range(1000000):
        val = bt.random().value
        randomness_dict[val] = randomness_dict.get(val, 0) + 1

    print(randomness_dict)

