class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
def sortTemperatureList(head):
  if not head or not head.next:
    return head
  prev=head
  curr=head.next
  while curr:
    if curr.data<0:
      prev.next=curr.next
      curr.next=head
      head=curr
      curr=prev.next
    else:
      prev=curr
      curr=curr.next
  return head
def createLinkedList(arr):
  head=Node(arr[0])
  curr=head
  for val in arr[1:]:
    curr.next=Node(val)
    curr=curr.next
  return head
def printList(head):
  while head:
    print(head.data,end=" - " if head.next else "")
    head=head.next
  print()
arr=list(map(int,input("enter temp values: ").split()))
head=createLinkedList(arr)
sorted_head=sortTemperatureList(head)
print("Sorted by actual values: ")
printList(sorted_head)



  
  






