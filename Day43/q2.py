n=int(input())
adj=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n
res=[]
def dfs(u):
  visited[u]=True
  res.append(u)
  for v in adj[u]:
    if not visited[v]:
      dfs(v)
dfs(0)
print(res)
  