def reverse_with_stack(s):
  stack=[]
  for char in s:
    stack.append(char)
  reversed_s=''
  while stack:
    reversed_s +=stack.pop()
  return reversed_s
input_str=input()
print(reverse_with_stack(input_str))











