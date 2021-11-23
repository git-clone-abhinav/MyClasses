# https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues

# Python Queue Class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items
    
    def __add__(self, other):
        return self.items + other
    
    def __radd__(self, other):
        return other + self.items

    
# Test
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q[0])
    q[0] = 'a'
    print(q)
    print(len(q))
    print(q.isEmpty())
    print(q.peek())
    print(q.size())
    print(q)
    q.dequeue()
    print(q)
    print(q.size())
    print(q.isEmpty())
    print(q.peek())
    print(q.size())
    print(q)
    q.enqueue(5)
    print(q)
    print(q.size())
    print(q.isEmpty())
    print(q.peek())
    print(q.size())
    print(q)
    print(q + [6, 7, 8])
    print(q)
    print(q.size())
    print(q.isEmpty())
    print(q.peek())
    print(q.size())
    print(q)
    print(q.items)
    print(q.__str__())
    print(q.__repr__())
    print(q.__len__())
    print(q.__getitem__(0))
    print(q.__setitem__(0, 'b'))
    print(q)
    print(q.__delitem__(0))
    print(q)
    print(q.size())
    print(q.isEmpty())
    print(q.peek())
    print(q.size())
    print(q)
    for i in q:
        print(i)
    print(1 in q)
    print(2 in q)
    print(3 in q)
    print(4 in q)
    print(5 in q)
    print(6 in q)