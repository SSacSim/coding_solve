import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for i in range(T):
  doc_num, location = map(int,input().split(" "))
  important = list(map(int,input().split(" ")))
  target_impor = important[location]
  raw_important = important.copy()
  raw_important.sort(reverse = True)
  my_q = deque([]) #

  for index, i in enumerate(important):
    if index == location:
      my_q.append([i,1])
    else:
      my_q.append([i,0])
  
  count = 0
  max_index = 0
  k = 0
  while True:
    if len(my_q) == 0:
      break
    pop_impor = my_q.popleft()
    if pop_impor[1] == 1 and raw_important[max_index] == target_impor:
      count += 1
      break

    if pop_impor[0] != raw_important[max_index]:
      my_q.append(pop_impor)
    else:
      max_index +=1
      count += 1
  print(count)
