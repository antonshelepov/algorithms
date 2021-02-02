# Implement a Queue using 2 Stacks
# Key Insight is that a stack reverses order <-> queue doesn't

# IMPORTANT!!

class Queue2Stacks(object):

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def enqueue(self,elem):

        # Add an enqueue with the "IN" stack
        self.stack1.append(elem)
        

    def dequeue(self,elem):
        if not self.stack2:
            while self.stack1:
                # Add the elements to stack2 to reverse the order when called
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue(i))
