# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/submissions/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        pre_sum = 0
        seen = {}
        while curr:
            pre_sum += curr.val
            if pre_sum not in seen:
                seen[pre_sum] = curr
            else:
                node = seen[pre_sum]
                node.next = curr.next
                while list(seen.keys())[-1] != pre_sum:
                    seen.popitem()
            curr = curr.next
        return dummy.next
