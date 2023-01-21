cacheSize = 2
cities = ["Jeju", "Jeju", "Jeju", "Jeju"]

from collections import deque

my_que = deque([])
my_que = deque([])
runtime = 0
for i in cities:
  i = i.lower()
  if i not in my_que:
    
    print(my_que)
    print("===============")
    my_que.append(i)

    if len(my_que) >cacheSize:
      my_que.popleft()

    runtime += 5
  else:
    my_que.remove(i)
    my_que.append(i)
    runtime += 1
  

print(runtime)