"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c
"""

class Node:
    def __init__(self, project):
        self.project = project
        self.dependencies = set()
        self.dependents = set()

def build_order(projects, dependencies):
    proj_nodes = {p: Node(p) for p in projects}
    for first_proj, second_proj in dependencies:
        first, second = proj_nodes[first_proj], proj_nodes[second_proj]
        first.dependents.add(second)
        second.dependencies.add(first)

    order = []
    while proj_nodes:
        buildable = [p for p in proj_nodes.values() if not p.dependencies]
        if not buildable:
            raise "Cycle Found"
        for b in buildable:
            order.append(b.project)
            for dep in b.dependents:
                dep.dependencies.remove(b)
            del proj_nodes[b.project]

    return order

if __name__ == '__main__':
    projects = "a b c d e f".split()
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print(build_order(projects, dependencies))

