from collections import deque
n=int(input())
adj=[list(map(int,input().split())) for _ in range(n)]
visited=[False] *n
queue=deque([0])
visited[0]=True
res=[]
while queue:
  node=queue.popleft()
  res.append(node)
  for nei in adj[node]:
    if not visited[nei]:
      visited[nei]=True
      queue.append(nei)
print(res)
  