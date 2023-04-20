class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self, node):
        if node:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Pre-order traversal of binary tree is:")
tree.pre_order(tree.root)
