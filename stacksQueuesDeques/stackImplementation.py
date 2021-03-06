# Last in first out 

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

s = Stack()
s.push(5)
s.push("eleven")
print(s.isEmpty())
print(s.size())
print(s.peek())
print(s.show())
