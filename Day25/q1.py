def can_unlock(n,stones,target):
  stones.sort()
  for i in range(n-2):
    left=i+1
    right=n-1
    while left<right:
      current_sum=stones[i]+stones[left]+stones[right]
      if current_sum==target:
        return True
      elif current_sum<target:
        left +=1
      else:
        right -=1

  return False

n=int(input())
stones=list(map(int,input().split()))
target=int(input())
print(str(can_unlock(n,stones,target)).lower())



















