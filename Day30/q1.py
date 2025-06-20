S=input().strip()
x=y=slips=0
visited={(0,0)}
for move in S:
  if move=='L':x-=1
  elif move=='R':x+=1
  elif move=='U':y+=1
  elif move=='D':y-=1
  if (x,y) in visited:
    slips +=1
  else:
    visited.add((x,y))
print(slips)



