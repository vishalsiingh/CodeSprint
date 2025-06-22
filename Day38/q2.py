def find_symbol(n,k):
  if n==1:
    return 0
  mid=2**(n-2)
  if k<=mid:
    return find_symbol(n-1,k)
  else:
    return 1 -find_symbol(n-1,k-mid)
n,k=map(int,input().split())
print(find_symbol(n,k))

