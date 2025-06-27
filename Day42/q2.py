class T:
  def __init__(s,v): s.val,s.left,s.right=v,None,None
def bst(a):
  if not a: return None
  m=len(a)//2
  r=T(a[m])
  r.left=bst(a[:m])
  r.right=bst(a[m+1:])
  return r
def lvl(r):
  from collections import deque as d
  q,res=d([r]),[]
  while q:
    n=q.popleft()
    if n: res += [n.val]; q+= [n.left,n.right]
    else: res += [None]
  while res and res[-1] is None: res.pop()
  return res
print(lvl(bst(list(map(int,input().split())))))





