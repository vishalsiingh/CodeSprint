from collections import  Counter
def sort_by_frequency(n,arr):
  freq=Counter(arr)
  arr.sort(key=lambda x:(-freq[x],x))
  return arr
n=int(input())
arr=list(map(int,input().split()))
result=sort_by_frequency(n,arr)
print(' '.join(map(str,result)))


