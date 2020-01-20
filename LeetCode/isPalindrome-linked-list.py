# Given a singly linked list, determine if it is a palindrome.
# https://leetcode.com/problems/palindrome-linked-list/


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: Node) -> bool:
        a_string = []
        while head != None:
            a_string.append(head.val)
            head = head.next
        if a_string == a_string[::-1]:
            return True
        else:
            return False


a = Node(2)
a.next = Node(1)
a.next.next = Node(2)

print(Solution().isPalindrome(a))
