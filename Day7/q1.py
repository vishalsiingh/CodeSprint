def count_movement_segmment(log):
  count=0
  i=0
  n=len(log)
  while i<n:
    if log[i]=='1':
      count+=1
      while i<n and log[i]=='1':
        i+=1
    else:
      i+=1
  return count
log=input("Enter movementlog :").strip()
print(" Number of Movements",count_movement_segmment(log))
        