class T:
  def __init__(s,v):s.val,s.left,s.right=v,None,None
def build(a):
  from collections import deque as d
  q,i,r=d(),1,T(a[0]);q.append(r)
  while i<len(a):
    n=q.popleft()
    if a[i] is not None: n.left=T(a[i]); q.append(n.left)
    i +=1
    if i <len(a) and a[i] is not None: n.right=T(a[i]); q.append(n.right)
    i +=1
  return r
def count(n):
  if not n: return 0
  lh=rh=0; l=r=n
  while l:lh +=1;l=l.left
  while r:rh +=1; r=r.right
  return (1 <<lh) -1 if lh ==rh else 1 +count(n.left) + count(n.right)
a=[int(x) if x !='null' else None for x in input().split()]
print(count(build(a)))