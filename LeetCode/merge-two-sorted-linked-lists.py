# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        dummyNode = ListNode(0)
        pre = dummyNode

        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        # if still remaining in either l1 or l2
        if not l1:
            pre.next = l2
        elif not l2:
            pre.next = l1
        # pre.next = l1 or l2

        return dummyNode.next
