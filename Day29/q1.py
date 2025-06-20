def can_cure_all_patients(n,vaccines,patients):
  vaccines.sort()
  patients.sort()
  for i in range(n):
    if vaccines[i]<=patients[i]:
      return "No"
  return "Yes"
n=int(input())
vaccines=list(map(int,input().split()))
patients=list(map(int,input().split()))

print(can_cure_all_patients(n,vaccines,patients))





