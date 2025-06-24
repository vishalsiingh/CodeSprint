def count_good_digit(i,n):
  if i==n:
    return 1
  if i%2 ==0:
    return 5 * count_good_digit(i+1,n)
  else:
    return 4* count_good_digit(i+1,n)
n=int(input("Enter the lengeth of digit string: "))
result=count_good_digit(0,n)
print("Total good digits strings: ",result)