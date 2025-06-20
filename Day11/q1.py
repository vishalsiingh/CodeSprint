def zigzag_reorder(appointments):
  result=[]
  left,right=0,len(appointments)-1
  while left<=right:
    if left==right:
      result.append(appointments[left])
    else:
      result.append(appointments[left])
      result.append(appointments[right])
    left +=1
    right -=1
  return result
appointments=list(map(int,input("enter appointments: ").split()))
reordered=zigzag_reorder(appointments)
print("Zig-Zag: ",reordered)
















