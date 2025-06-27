def power(x,n):
  if n==0: return 1
  if n<0: return 1/power(x,-n)
  half=power(x,n//2)
  return half*half if n%2==0 else half* half*x
x=float(input())
n=int(input())
print(f"{power(x,n):.5f}")