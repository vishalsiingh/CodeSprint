class Node:
  def __init__(self,val): self.val,self.prev,self.next=val,None,None
def build_dll(vals):
  head=prev=None
  for v in vals:
    node=Node(v)
    if not head: head=node
    if prev:prev.next,node.prev=node,prev
    prev=node
  return head
def remove_cursed(head,target):
  curr=head
  while curr:
    nxt=curr.next
    if curr.val==target:
      if curr.prev: curr.prev.next=curr.next
      else: head=curr.next
      if curr.next: curr.next.prev=curr.prev
    curr=nxt
  return head
def print_dll(head):
  res=[]
  while head: res.append(str(head.val)); head.next
  print("->".join(res) if res else "(empty list)")
vals=list(map(int,input("Beads: ").split()))
target=int(input("cursed numbr: "))
print_dll(remove_cursed(build_dll(vals),target))










