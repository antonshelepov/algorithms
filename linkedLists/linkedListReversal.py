# 

class Node(object):

    def __init__(self,value):

        self.value = None
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

reverse(a)
