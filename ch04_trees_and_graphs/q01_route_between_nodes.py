"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

from graph import Node
from collections import deque

def route_between(node1, node2):
    node1.visited = True
    queue = deque()
    queue.append(node1)
    while queue:
        node = queue.popleft()
        if node == node2:
            return True
        for adj in node.adjacents:
            if not adj.visited:
                adj.visited = True
                queue.append(adj)

    return False

if __name__ == '__main__':
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    def refresh_visited():
        n0.visited = n1.visited = n2.visited = n3.visited = n4.visited = n5.visited = False

    n0.adjacents = [n1, n4, n5]
    n1.adjacents = [n3, n4]
    n2.adjacents = [n1]
    n3.adjacents = [n2, n4]

    print(route_between(n0, n2))
    refresh_visited()
    print(route_between(n5, n2))
    refresh_visited()
    print(route_between(n3, n4))
    refresh_visited()
    print(route_between(n4, n2))

