from bisect import bisect_left,insort
n=int(input())
seen=[]
for _ in range(n):
  w=input().strip()
  print(bisect_left(seen,w))
  insort(seen,w)