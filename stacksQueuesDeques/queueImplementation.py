# First in first out

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

q = Queue()

print(q.size())
q.enqueue(1)
q.enqueue(5)
q.enqueue(8)
q.enqueue(3)

print(q.size())
q.dequeue()
print(q.show())
