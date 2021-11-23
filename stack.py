# https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks

# Python Stack Class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
# Test
if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)