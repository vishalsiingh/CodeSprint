class ListNode:
    def __init__(self, val): self.val, self.next = val, None

def to_linked(lst):
    dummy = ListNode(0)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    for _ in range(left - 1): prev = prev.next
    cur = prev.next
    for _ in range(right - left):
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp
    return dummy.next

items = input("Enter shopping list (comma-separated): ").split(",")
left = int(input("Enter left index: "))
right = int(input("Enter right index: "))

head = to_linked([item.strip() for item in items])
res = reverseBetween(head, left, right)


print("Updated list:", to_list(res))
