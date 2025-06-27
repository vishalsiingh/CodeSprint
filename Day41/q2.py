from collections import deque
class TreeNode:
  def __init__(self,val):self.val=val;self.left=self.right=None
def build(vals):
  nodes=[None if v =='null' else TreeNode(int(v)) for v in vals]
  kids=deque(nodes[1:])
  for node in nodes:
    if node:
      if kids:node.left=kids.popleft()
      if kids: node.right=kids.popleft()
    return nodes[0]
def isMirror(t1,t2):
  if not t1 and not t2:return True
  if not t1 or not t2:return False
  return t1.val==t2.val and isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
vals=input().split()
print(str(isMirror(r:=build(vals).left,build(vals).right)).lower())
