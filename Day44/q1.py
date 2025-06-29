s=input()
t=input()
def is_valid(s,t):
  return len(s) ==len(t) and len(set(zip(s,t))) ==len(set(s))==len(set(t))
print(is_valid(s,t))