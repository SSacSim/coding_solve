people  = [70, 80, 50]
limit = 100

from collections import deque
people.sort()

my_que = deque(people)

print(my_que)
count = 0
while True:
  print(my_que)
  if len(my_que) == 0:
    break
  
  if len(my_que) == 1:
    count += 1
    break

  left = my_que.popleft()
  right = my_que.pop()

  if (left + right) > limit:
    my_que.appendleft(left)
    count +=1
  else:
    count +=1