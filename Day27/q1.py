score=list(map(int,input().split(',')))
rank={s:str(i+1) for i,s in enumerate(sorted(score,reverse=True))}
for i,s in enumerate(sorted(score,reverse=True)[:3]):
  rank[s]=["Gold Medal","Silver Medal","Bronze Medal"][i]
print([rank[s] for s in score])



