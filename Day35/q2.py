from collections import Counter
n=int(input())
a=[int(input()) for _ in range (n)]
print(max(Counter(a).values()))