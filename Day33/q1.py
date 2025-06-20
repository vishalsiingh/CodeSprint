from collections import Counter
def can_split_clubs(N,K,themes):
  freq=Counter(themes)
  at_least_two=sum(1 for count in freq.values() if count >=2)
  only_one=sum(1 for count in freq.values() if count ==1)
  max_assignable=2*at_least_two+only_one
  
  if max_assignable >= 2*K:
    print("Yes")
  else:
    print("No")
N,K=map(int,input().split())
themes=list(map(int,input().split()))
can_split_clubs(N,K,themes)




