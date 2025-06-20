class Node:
    def __init__(self,v):
        self.val=v
        self.next=None

def split(head,k):
    n=0;cur=head
    while cur: n+=1; cur=cur.next
    base, rem = divmod(n,k)
    parts=[]; cur=head
    for i in range(k):
        parts.append(cur)
        size = base + (1 if i<rem else 0)
        for _ in range(size-1):
            if cur: cur=cur.next
        if cur:
            nxt=cur.next
            cur.next=None
            cur=nxt
    return parts

def build(arr):
    dummy=Node(0)
    cur=dummy
    for x in arr:
        cur.next=Node(x)
        cur=cur.next
    return dummy.next

def printParts(parts):
    out=[]
    for p in parts:
        vals=[]
        while p:
            vals.append(str(p.val))
            p=p.next
        out.append("["+ ", ".join(vals)+"]" if vals else "[]")
    print(" , ".join(out))

tasks=list(map(int,input().split()))
k=int(input())
head=build(tasks)
printParts(split(head,k))
