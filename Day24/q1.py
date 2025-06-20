from collections import deque
def first_non_repeating(s):
  result=[]
  q=deque()
  count={}
  for ch in s:
    count[ch] =count.get(ch,0) + 1
    q.append(ch)
    while q and count[q[0]]>1:
      q.popleft()
    if q:
      result.append(q[0])
    else:
      result.append('#')
  return ''.join(result)
s=input("ENTER the stirng of lowercase: ")
output=first_non_repeating(s)
print("output:", output)






















