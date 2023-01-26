numbers = [2, 3, 3, 5]
new_numbers =[] # (값 , index)로 저장 

for index,i in enumerate(numbers):
  new_numbers.append([i,index])

store =[]
answer= [-1 for _ in range(len(numbers))]
for i in new_numbers: 
  if len(store) == 0:
    store.append(i)
    continue
  
  value = i[0]
  index = i[1]
  
  while True:
    pop_store = store.pop()
    pop_value = pop_store[0]
    pop_index = pop_store[1]

    if value <= pop_value :
      store.append(pop_store)
      store.append(i)
      break
    else:
      answer[pop_index] = value
    if len(store) == 0:
      store.append(i)
      break
  
  print("store",store)
  print("answer",answer)
  print("===================================")