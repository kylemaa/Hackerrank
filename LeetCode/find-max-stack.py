class MaxStack(object):
    # maxes stack holds the current max value.
    def __init__(self, *args, **kwargs):
        self.stack = []
        self.maxes = []

    def push(self,val):
        self.stack.append(val)
        if self.maxes and self.maxes[-1]> val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop()) 