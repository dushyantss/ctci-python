class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

def in_order(node, visit):
    if node:
        in_order(node.left, visit)
        visit(node)
        in_order(node.right, visit)

def pre_order(node, visit):
    if node:
        visit(node)
        pre_order(node.left, visit)
        pre_order(node.right, visit)

def post_order(node, visit):
    if node:
        post_order(node.left, visit)
        post_order(node.right, visit)
        visit(node)

