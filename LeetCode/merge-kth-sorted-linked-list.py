class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    arr = []
    # append all the node values into a empty list
    for node in lists:
        while node:
            arr.append(node.val)
            node = node.next
    head = root = None
    # sort the values in the array and put them into a linked list
    for val in sorted(arr):
        if not root:
            head = root = Node(val)
        else:
            root.next = Node(val)
            root = root.next
    return head


def merge2(lists):
    head = current = Node(-1)
    while any(list is not None for list in lists):
        current_min, i = min((list.val, i)
                             for i, list in enumerate(lists) if list is not None)
    lists[i] = lists[i].next
    current.next = Node(current_min)
    current = current.next
    return head.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
# 135
print(b)
# 246
print(merge2([a, b]))
# 123456
