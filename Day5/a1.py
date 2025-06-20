from collections import Counter
def check_emotional_balance(s):
  freq=Counter(s)
  values=list(freq.values())
  if all(val==values[0] for val in values):
    print("Aashriya smiles:Emotional balance found.")
  else:
    print("Aashriya wonders: These thoughts were scattered.")
s=input("Enter a String: ").strip()
check_emotional_balance(s)