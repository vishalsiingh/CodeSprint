def next_char(c):
  return chr(((ord(c) - ord('a') +1 ) %26)+ ord('a'))
def solve(k):
  s="a"
  while len(s) <k:
    shifted=''.join(next_char(c) for c in s)
    s += shifted
  print(s[k-1].upper())
k=int(input())
solve(k)