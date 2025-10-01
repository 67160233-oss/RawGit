class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def is_empty(self):
        return len(self.list) == 0


    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.list.pop()

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        return "Stack is empty"

    def size(self):
        return len(self.list)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Size after push:",s.size())
print("Top element:", s.peek())

print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())

print("Is empty?",s.is_empty())
print("Pop from empty:",s.pop())