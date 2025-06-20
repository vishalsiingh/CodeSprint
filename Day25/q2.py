from functools import cmp_to_key
def compare(x,y):
  if x+y>y+x:
    return -1
  elif x+y<y+x:
    return 1
  else:
    return 0
def largest_number(arr):
  arr=list(map(str,arr))
  arr.sort(key=cmp_to_key(compare))
  if arr[0]=='0':
    return '0'
  return ''.join(arr)
n=int(input())
arr=list(map(int,input().split()))
print(largest_number(arr))






























