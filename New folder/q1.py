class ListNode:
  def __init__(self,val=0,next=None):self.val,self.next=val,next
def build(nums):
  head=ListNode(0)
  curr=head
  for n in nums: curr.next,curr=ListNode(n),curr.next
  return head.next
def add(l1,l2):
  head=ListNode(0)
  curr,carry=head,0
  while l1 or l2 or carry:
    v1, v2=l1.val if l1 else 0,l2.val if l2 else 0
    carry,val= divmod(v1+v2+carry,10)
    new_node=ListNode(val)
    curr.next=new_node
    curr=new_node
    l1=l1.next if l1 else None
    l2=l2.next if l2 else None
  return head.next
def to_list(node):
  res=[]
  while node: 
    res.append(node.val)
    node=node.next
  return res
l1=build(map(int,input("Enter first number:").split()))
l2=build(map(int,input("Enter second number:").split()))
print(to_list(add(l1,l2)))








