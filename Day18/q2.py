def evaluatePostfix(arr):
  stack=[]

  for token in arr:
    if token in {"+","-","*","/"}:
      b=stack.pop()
      a=stack.pop()
      if token =="+":
        result=a+b
      elif token =="-":
        result =a-b
      elif token=="*":
        result=a*b
      elif token=="/":
        result=int(a/b)
      stack.append(result)
    else:
      stack.append(int(token))
  return stack[0]
arr=input("Enter postfix expression : ").split()
print(evaluatePostfix(arr))




















