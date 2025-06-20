def count_beautiful_pairs(n,cards):
  unique_card=sorted(set(cards))
  total=0
  for i in range (1,len(unique_card)):
    total +=i
  return total

n=int(input())
cards=list(map(int,input().split()))
print(count_beautiful_pairs(n,cards))




