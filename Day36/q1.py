def total_magic(n):
  a=1
  r=1/3
  total=a*(1-r**n)/(1-r)
  return round(total,5)
n=int(input())
print(total_magic(n))





