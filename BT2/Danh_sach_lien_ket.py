class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val, end=" ")
            curr_node = curr_node.next

linked_list = LinkedList()
linked_list.add_node(5)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.print_list()

