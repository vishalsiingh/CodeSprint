def is_vowel(name):
 return name[0] in 'aeiou'
n=int(input("Enter number of patient entries:"))
seen=set()
unique_vowel_patients=[]

for _ in range(n):
 name=input().strip()
 if is_vowel(name) and name not in seen:
    seen.add(name)
    unique_vowel_patients.append(name)

print(len(unique_vowel_patients))
for name in unique_vowel_patients:
  print(name)
