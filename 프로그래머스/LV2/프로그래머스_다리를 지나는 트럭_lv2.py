bridge_length = 100
weight = 100
truck_weights =[10,10,10,10,10,10,10,10,10,10]

from  collections import deque
truck_w = deque(truck_weights)
finish_que = deque([])
ing_que = deque([])

now_time = 0
now_weight = 0

answer = 0
count = 0
while True:

  if len(finish_que) == len(truck_weights):
    answer = now_time
    break

  now_time += 1
  if len(truck_w) != 0:
    input_truck = truck_w.popleft() # 다음 들어올 트럭
  else: 
    input_truck = None

  for i in range(len(ing_que)): # 시간이 지났으니 1증가
    ing_que[i][1] +=1

  # 빠져나가는 트럭
  if len(ing_que) != 0:
    pop_ing = ing_que.popleft()
    if pop_ing[1] != bridge_length: # 시간이 나갈 시간이 안됐으면 
      ing_que.appendleft(pop_ing) # 다시 넣음
    else:
      finish_que.append(pop_ing[0])
      now_weight -= pop_ing[0]

  # 들어오는 트럭  
  if input_truck != None and weight >= now_weight + input_truck: # 다리에 올라갈 수 있을때 
    ing_que.append([input_truck, 0])
    now_weight += input_truck
  else:
    truck_w.appendleft(input_truck)
  
  print("now_time",now_time)
  print("ing_que",ing_que)
  print("finish_que",finish_que)
  print("================")

print(answer)