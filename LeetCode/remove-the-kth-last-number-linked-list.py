class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        n = self
        answer = ''
        while n:
            answer += str(n.val)
            n = n.next
        return answer


def remove_kth(node, k):
    slow_ptr, fast_ptr = node, node
    for _ in range(k):
        fast_ptr = fast_ptr.next
    if not fast_ptr:
        return node.next
    prev = None

    while fast_ptr:
        prev = slow_ptr
        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
    prev.next = slow_ptr.next
    return node


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
# 12345
head = remove_kth(head, 4)
print(head)
# 1234
