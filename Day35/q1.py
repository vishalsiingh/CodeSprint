def minimize_max_box(n,k,a):
  def can(mid):
    group,curr =1,0
    for w in a:
      if curr +w> mid:
        group +=1
        curr=0
      curr +=w
    return group <=k
  l,r=max(a),sum(a)
  while l<=r:
    m=(l+r)//2
    if can(m): r=m-1
    else: l=m+1
  return 1
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(minimize_max_box(n,k,a))
















