def closest_triplet_sum(n,arr,target):
  arr.sort()
  closest_sum=float('inf')
  min_diff=float('inf')
  for i in range(n-2):
    left=i+1
    right=n-1
    while left<right:
      curr_sum=arr[i]+arr[left] +arr[right]
      diff=abs(curr_sum-target)
      if diff <min_diff or (diff ==min_diff and curr_sum>closest_sum):
        closest_sum=curr_sum
        min_diff=diff
      if curr_sum< target:
        left +=1
      else:
        right -=1
  return closest_sum
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(closest_triplet_sum(n,arr,target))

          
  

















