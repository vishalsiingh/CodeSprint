def is_operator(c):
  return c in '+-*/'
def postfix_to_prefix(postfix):
  stack=[]
  for char in postfix:
    if is_operator(char):
      right=stack.pop()
      left=stack.pop()
      expr=char+left+right
      stack.append(expr)
    else:
      stack.append(char)
  return stack[0]
postfix_expr=input()
print(postfix_to_prefix(postfix_expr))







