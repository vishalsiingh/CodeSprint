from collections import deque
def predictPartyVictory(senate):
  n=len(senate)
  radiant=deque()
  dire=deque()
  for i,s in enumerate(senate):
    if s=='R':
      radiant.append(i)
    else:
      dire.append(i)
  while radiant and dire:
    r=radiant.popleft()
    d=dire.popleft()
    if r<d:
      radiant.append(r+n)
    else:
      dire.append(d+n)
  return "Radiant" if radiant else "Dire"
senate=input("Enter a string: ")
print("Winner: ",predictPartyVictory(senate))
      






















