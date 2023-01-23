prices = [5,4,3,2,1] 	
store = [] # [index, 실제값]
answer= [ 0 for _ in range(len(prices))]

count = 0
for i_index,i in enumerate(prices):
  print("===================")
  print("store",store)
  print("price",i)
  if len(store) == 0:
    store.append([i_index,i])
    count += 1
    continue
  
  while True:
    if len(store) == 0:
      store.append([i_index, i])
      break
    top = store.pop()
    print("top",top)
    if top[1] > i: #중지
      answer[top[0]] = i_index - top[0]
    else:
      store.append(top)
      store.append([i_index, i])
      break

for i in store:
  answer[i[0]] = len(prices) - i[0] - 1
  
print(answer)
