numbers = [4, 1, 2, 1]
target = 4

# bfs

from collections import deque

my_que = deque([])

for i in numbers:
  print(my_que)
  if len(my_que) == 0:
    my_que.append(i)
    my_que.append(-i)
    continue


  temp_list = []
  while True:
    print("tmep_list",temp_list)
    if len(my_que) == 0:
      my_que = deque(temp_list)    
      break

    pop_number = my_que.popleft()
    print("pop_number",pop_number)
    temp_list.append(pop_number + i)
    temp_list.append(pop_number - i)
  
  print("====================")

count = 0
for i in my_que:
  if i == target:
    count += 1
print(count)