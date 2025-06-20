n=int(input())
merlin_spells=list(map(int,input().split()))

m=int(input())
morgana_spells=list(map(int,input().split()))
max_morgana=max(morgana_spells)
required_power=max_morgana+1
mana=sum(max(0,required_power-power) for power in merlin_spells)
print(mana)











