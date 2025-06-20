a=input().split();c=0
for i in range(len(a)-1,-1,-1):c+=int(a[i])*2;a[i]=str(c%10);c//=10
print(([str(c)]+a if c else a))