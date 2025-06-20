nums=list(map(int,input().split(',')))
dup=sum(nums)-sum(set(nums))
miss=sum(range(1,len(nums)+1))-sum(set(nums))

print([dup,miss])











