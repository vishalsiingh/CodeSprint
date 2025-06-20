nums=list(map(int,input("Enter badge number: ").split()))
n=len(nums)
print(n*(n+1)//2 - sum(nums))


