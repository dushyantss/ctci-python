"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
"""

def paths_with_sum(root, target):
    return paths_with_sum(root, target, 0, {0: 1}) # add 0: 1 for a path from root

def paths_with_sum(node, target, running_sum, path_count):
    if not node:
        return 0

    running_sum += node.value
    required_sum = running_sum - target
    count = path_count.get(required_sum, 0)

    path_count[running_sum] = path_count.get(running_sum, 0) + 1
    count += paths_with_sum(node.left, target, running_sum, path_count)
    count += paths_with_sum(node.right, target, running_sum, path_count)
    path_count[running_sum] = path_count[running_sum] - 1

    return count



