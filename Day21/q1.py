def time_to_buy_tickets(tickets,k):
  target=tickets[k]
  total_time=0
  for i in range(len(tickets)):
    if i<=k:
      total_time += min(tickets[i],target)
    else:
      total_time += min(tickets[i],target-1)
  return total_time
tickets=list(map(int,input("Enter tickets in array: ").split()))
k=int(input("Enter the position k:"))
print("total time to finish at positon ",k,"is:",time_to_buy_tickets(tickets,k))
















