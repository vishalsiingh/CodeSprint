
class Node:
  def __init__(self,val):
    self.val=val
    self.next=None
def detect_and_remove_loop(head):
  slow=fast=head
  while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
      slow=head
      if slow==fast:
        while fast.next !=slow:
          fast=fast.next
      else:
        while slow.next !=fast.next:
          slow=slow.next
          fast=fast.next
      fast.next=None
      return True
    return True
n=int(input("Number of nodes: "))
vals=list(map(int,input("Enter Node values: ").split()))
pos=int(input("Enter loop positon: "))

head=Node(vals[0])
curr=head
nodes=[head]
for v in vals[1:]:
  curr.next=Node(v)
  curr=curr.next
  nodes.append(curr)
if pos>0:
  curr.next=nodes[pos-1]
print(detect_and_remove_loop(head))














