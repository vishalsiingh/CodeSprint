def reverse_queue():
  n=int(input("Enter number of citizens: "))
  ids=list(map(int,input("Enter the IDs: ").split()))
  if len(ids) !=n:
    print("Error:Number of ids not match the given count.")
    return
  reversed_ids =ids[::-1]
  print("Reversed queue: ")
  print(' '.join(map(str,reversed_ids)))
reverse_queue()












