n=int(input())
words=[input().strip() for _ in range(n)]
masks=[]
for word in words:
  mask=0
  for ch in set(word):
    mask|=1 << (ord(ch) -ord('a'))
  masks.append((mask,len(word)))
max_strength =0
for i in range(n):
  for j in range(i+1,n):
    if masks[i][0] & masks[j][0]==0:
      max_strength =max(max_strength,masks[i][1] * masks[j][1])
print(max_strength)