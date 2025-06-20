from collections import deque
def max_score(nums,k):
  n=len(nums)
  dp=[0]*n
  dp[0]=nums[0]
  dq=deque([0])
  for i in range(1,n):
    while dq and dq[0] <i-k:
      dq.popleft()
    dp[i] =nums[i]+dp[dq[0]]
    while dq and dp[i]>=dp[dq[-1]]:
      dq.pop()
    dq.append(i)
  return dp[-1]
nums=list(map(int,input("Enter room value: ").split()))

k=int(input("Enter max jump length: "))
print("Max score :",max_score(nums,k))











