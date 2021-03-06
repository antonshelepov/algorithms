# given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle"

from nose.tools import assert_equal

class Node(object):
    
    def __init__(self,value):

        self.value = value
        self.nextnode = None

def cycle_check(node):

    mark1 = node
    mark2 = node

    while mark1 != None and mark2.nextnode != None:

        mark1 = mark1.nextnode
        mark2 = mark2.nextnode.nextnode

        if mark2 == mark1:
            return True

    return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
        
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
                                    
print("ALL TEST CASES PASSED")
                                                    

t = TestCycleCheck()
t.test(cycle_check)
