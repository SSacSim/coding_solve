from collections import deque
priorities = [2, 1, 3, 2]	
sort_priorites = priorities.copy()
sort_priorites.sort(reverse = True)
location = 2
from collections import deque

my_que = deque([])

for index, i in enumerate(priorities):
  my_que.append([index, i ])


my_que = deque([])

for index, i in enumerate(priorities):
  my_que.append([index, i ])

max_index = 0
count = 0
while True:
  pop_index, pop_number = my_que.popleft()
  print(pop_number)
  if pop_number == sort_priorites[max_index] and pop_index == location:
    answer = count +1
    count += 1
    max_index += 1
    break

  if pop_number == sort_priorites[max_index] :
    count += 1
    max_index += 1
  
  my_que.append([pop_index, pop_number])
print(answer)
