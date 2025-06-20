class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = cur = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def to_linked_list(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


list1 = list(map(int, input("Enter elements of first sorted list (space-separated): ").split()))
list2 = list(map(int, input("Enter elements of second sorted list (space-separated): ").split()))


l1 = to_linked_list(list1)
l2 = to_linked_list(list2)


merged = mergeTwoLists(l1, l2)
print("Merged List:", to_list(merged))
