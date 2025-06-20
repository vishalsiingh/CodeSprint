n=int(input("Enter the number of days:"))
count=0
if n>10:
  print("Abhik's marathon journey intensifies! Let's see his detailed zig zag pattern:")
for day in range(1,n+1):
  num_count=day
  max_width=(n-1)*4
  current_width=(num_count-1)*4
  spaces=(max_width-current_width)//2

  print(" " * spaces,end="")

  if day%2==1:
    for i in range(1,day+1):
      print(i,end="")
      count+=1
      if i!=day:
        print("   ",end="")
  else:
    for i in range(day,0,-1):
      print(i,end="")
      count +=1
      if i!=1:
        print("   ",end="")
  print()
print("Total numbers printed:",count)
    
