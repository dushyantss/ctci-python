from collections import deque

class Graph:
    def __init__(self):
        self.nodes = []

class Node:
    def __init__(self, value):
        self.value = value
        self.adjacents = []

def dfs(node, visit):
    visit(node)
    node.visited = True
    for adj in node.adjacents:
        if not adj.visited:
            dfs(adj, visit)

def bfs(node, visit):
    node.visited = True
    queue = deque()
    queue.append(node)
    while queue:
        popped = queue.popleft()
        visit(popped)
        for adj in popped.adjacents:
            if not adj.visited:
                adj.visited = True
                queue.append(adj)

