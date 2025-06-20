def exam_seating(n):
  count=0
  for i in range(n):
    row=[]
    for j in range (n):
      if(i+j)%2==0:
        row.append(1)
        count+=1
      else:
        row.append(0)
    print("".join(map(str,row)))
  print(f"Total students seated:{count}")
n=int(input(" Representation of rows and columns:"))
exam_seating(n)