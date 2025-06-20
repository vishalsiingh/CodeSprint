def min_flips(n,s):
  zero_count=s.count('0')
  misplaced_ones=sum(1 for i in range(zero_count) if s[i] == '1')
  misplaced_zeroes=sum(1 for  i in range(zero_count,n) if s[i] == '0')
  print(min(misplaced_ones,misplaced_zeroes))
n=int(input())
s=input()
min_flips(n,s)
