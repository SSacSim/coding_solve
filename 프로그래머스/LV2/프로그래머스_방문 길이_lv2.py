dirs = "LULLLLLLU"

visit_dict = dict() # [x,y] :[next_x,next_y] 형태로 저장 > 도착 : 출발 

now_x = 0
now_y = 0

count = 0
for i in dirs:
  if i == "U":
    next_x = now_x
    next_y = now_y - 1
  elif i == "R":
    next_x = now_x + 1
    next_y = now_y 
  elif i == "D":
    next_x = now_x
    next_y = now_y + 1
  else:
    next_x = now_x - 1
    next_y = now_y 

  if next_x >= -5 and next_x <= 5 and next_y <=5 and next_y >= -5:
    if (now_x,now_y,next_x,next_y) not in visit_dict: # 해당 경로를 이용하지 않았을때, 
      visit_dict[now_x,now_y,next_x,next_y] = 1 # 출발도착
      visit_dict[next_x,next_y,now_x,now_y,] = 1
      count += 1
      print((now_x,now_y,next_x,next_y))
    now_x = next_x
    now_y = next_y

print(count)