n=int(input())
arr=list(map(int,input().split()))
prefix=[1]*n
suffix=[1]*n
res=[1]*n
for i in range(1,n):
  prefix[i] =prefix[i-1]*arr[i-1]
for i in range(n-2,-1,-1):
  suffix[i] =suffix[i+1] *arr[i+1]
for i in range(n):
  res[i] =prefix[i] * suffix[i]
print(*res)
  