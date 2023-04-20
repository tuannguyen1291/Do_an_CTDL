class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.size())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.pop())
print(s.is_empty())
