elements = [7,9,1,1,4]
raw_data = elements.copy()
new_data = elements.copy()
start_index = 1

answer = []
answer.extend(elements)

while True:
  point_index = start_index
  print(point_index)
  if start_index >= len(elements):
    break

  store_temp = []
  print("raw_data",raw_data)
  print("new_data",new_data)
  flag= 0
  left_index = 0
  right_index = point_index
  while True: 
    if right_index == point_index and flag == 1:
      break
    if right_index >= len(elements):
      flag = 1
      right_index = 0

    
    print("더할때",raw_data[right_index] + new_data[left_index])
    print("index",left_index , right_index)
    store_temp.append(raw_data[right_index] + new_data[left_index])
    right_index += 1
    left_index += 1
  answer.extend(store_temp)
  new_data = store_temp.copy()
  start_index += 1

  print("=========================")

print(len(set(answer)))  