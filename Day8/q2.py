def min_len(target,s):
   l=t=res=0;ans=float('inf')
   for r in range(len(s)):
     t+=s[r]
     while t>=target: ans=min(ans,r-l+1);t-=s[l];l+=1
   return ans if ans!=float('inf') else '0'
target=int(input("Target:"))
sessions=list(map(int,input("Sessions:").split()))
print(min_len(target,sessions))
