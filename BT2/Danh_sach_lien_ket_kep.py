class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val, end=" ")
            curr_node = curr_node.next

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add_node(1)
doubly_linked_list.add_node(2)
doubly_linked_list.add_node(3)
doubly_linked_list.print_list()
