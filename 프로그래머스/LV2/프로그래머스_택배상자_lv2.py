from collections import deque
order =  [5, 4, 3, 2, 1]
target_index = 0
temp = deque([])
truck = []

box_number = 0
count = 0
k = 0
flag=0
while True:
  
  if box_number >= len(order):
    break

  box_number +=1
  print("box_number" , box_number)
  print("target_number" , order[target_index])
  if box_number < order[target_index]:
    temp.appendleft(box_number)
  
  elif box_number == order[target_index]:
    count += 1
    target_index +=1

  elif box_number > order[target_index]:
    box_number -=1
    pop_number = temp.popleft()
    if pop_number == order[target_index]:
      target_index +=1
      count +=1
    else:
      flag = 1
      break

if flag == 0 : 
  for i in temp:
    if i == order[target_index]:
      count +=1
      target_index +=1
    else:
      break

print(count)