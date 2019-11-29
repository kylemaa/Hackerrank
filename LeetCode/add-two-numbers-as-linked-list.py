class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # param of two lists with init value 0 
        return self.helper(l1, l2, 0)
    # this function update the carry over and return the next links if next is not null    
    def helper(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val//10
        ret = Node(val % 10)
        if l1.next != None or l2.next != None or c != 0:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)    
            ret.next = self.helper(l1.next, l2.next, c)
        return ret


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1,l2)
while answer: 
    # print the node and its links 
    print(answer.val)
    answer = answer.next