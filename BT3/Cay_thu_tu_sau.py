class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_tree():
    # Tạo một cây nhị phân đơn giản với cấu trúc như sau:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def pre_order_traversal(node):
    if node:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# Tạo cây
root = create_tree()

# In cây theo thứ tự trước
pre_order_traversal(root)
