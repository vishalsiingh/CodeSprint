n=int(input())
p=[0,0] + [1] *(n-1)
for i in range(2,int(n**0.5)+1):
  if p[i]: p[i*i:n+1:i] = [0]*len(p[i*i:n+1:i])
primes =[i for i ,v in enumerate (p) if v]
print(*[primes[i] for i in range(len(primes)) if p[i+1]])







