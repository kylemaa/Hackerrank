class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
    # this method would push the val into the first stack

    def enqueue(self, val):
        self.s1.append(val)

    # this method would dequeue the first stack by popping the first stack onto the second stack,
    # then it returns the top values by popping the second stack
    def dequeue(self):
        if self.s2:
            return self.s2.pop()
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        return None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3 4
