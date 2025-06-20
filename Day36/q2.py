def nCr(n,r,memo={}):
  if r==0 or r ==n:
    return 1
  if(n,r) in memo:
    return memo[(n,r)]
  memo[(n,r)]=nCr(n-1,r,memo) +nCr(n-1,r-1,memo)
  return memo[(n,r)]
n,r=map(int,input().split())
print(nCr(n,r))