text = input("Text: ")
pattern = input(" Pattern: ")
n, m = len(text), len(pattern)
b, mod = 31, 10**9 + 7
ph = sum((ord(c)-96)*pow(b,i,mod) for i,c in enumerate(pattern))%mod
th = sum((ord(text[i])-96)*pow(b,i,mod) for i in range(m))%mod
res = [0] if th==ph and text[:m]==pattern else []
bp = pow(b,mod-2,mod)
for i in range(1,n-m+1):
    th = (th - (ord(text[i-1])-96))*bp % mod
    th = (th + (ord(text[i+m-1])-96)*pow(b,m-1,mod)) % mod
    if th==ph and text[i:i+m]==pattern: res.append(i)
print(res)
