# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __str__(self):
        result = str(self.val)
        if self.next:
            result += str(self.next)
        return result

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None 
        curr = head 
        # while not the end of the linked list
        while curr != None:
            # hold the value of the next node
            temp = curr.next 
            # point the next node backwards
            curr.next = prev
            # move to the curr so we can point the next node to it 
            prev = curr 
            # now curr holds the value of temp
            curr = temp
        # return head
        return prev


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
print(Solution().reverseList(node))