# https://leetcode.com/problems/merge-two-sorted-lists/

"""This script merges two linked list into one sorted linked list"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lists = [l1, l2]
        array = []
        for node in lists:
            while node:
                array.append(node.val)
                node = node.next

        head = root = None
        for val in sorted(array):
            # head and root are going to point at the first node.
            if not root:
                head = root = ListNode(val)
            # if root is already pointed to a node, then assign val to root's nexts
            else:
                root.next = ListNode(val)
                root = root.next
        # return the head which has the print string method of all of its node
        return head


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(5)
print(Solution().mergeTwoLists(a, b))  # Should output 112233
