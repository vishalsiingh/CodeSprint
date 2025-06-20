class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def build_dll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        new_node = Node(val)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head

def print_dll(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(vals))

def sort_dll(head):
   
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
   
    vals.sort()   
    return build_dll(vals)
N = int(input())
arr = list(map(int, input().split()))


head = build_dll(arr)
sorted_head = sort_dll(head)
print_dll(sorted_head)
