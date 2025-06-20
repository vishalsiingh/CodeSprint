from collections import deque
def count_students_not_eat(n,students,sandwiches):
  queue=deque(students)
  i=0
  count=0
  while queue and count < len(queue):
    if queue[0]== sandwiches[i]:
      queue.popleft()
      i +=1
      count=0
    else:
      queue.append(queue.popleft())
      count +=1
  return len(queue)
n=int(input())
students=list(map(int,input().split()))
sandwiches=list(map(int,input().split()))

print(count_students_not_eat(n,students,sandwiches))
















