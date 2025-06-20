from collections import deque
def magician_deck(deck):
  deck.sort()
  res=deque()
  for card in reversed(deck):
    if res:
      res.appendleft(res.pop())
    res.appendleft(card)
  return list(res)

def reveal_order(deck):
  deck=deque(deck)
  result=[]
  while deck:
    result.append(deck.popleft())
    if deck:
      deck.append(deck.popleft())
  return result

deck=list(map(int,input("Enter the deck values: ").split()))
initial=magician_deck(deck)

print("Initial deck order:",initial)
print("Revealed deck order:",reveal_order(initial))












