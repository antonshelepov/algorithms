# new items can be added at either the front or the rear

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self_):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        # allows the item to be added to the end
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()

d.addFront('hello')
d.addRear('world')
