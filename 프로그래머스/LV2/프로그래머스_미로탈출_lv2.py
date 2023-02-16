maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOXE"]

visit = [[ 0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

# bfs
from collections import deque
start = []
end = []
laber = []
for i_index, i in enumerate(maps):
  for j_index, j in enumerate(i):
    if j == "S":
      start= [i_index , j_index]
    elif j == "E":
      end = [i_index , j_index]
    elif j == "L":
      laber= [i_index , j_index]
      
my_q = deque([[start , 0]]) # 좌표 / 

# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

laber_count = -1
find_laber = 0
while True:# laber 찾기
  print("===========================")
  print("my_q",my_q)

  if len(my_q)== 0 :
    break

  pop_value = my_q.popleft()
  print(pop_value)

  
  if maps[pop_value[0][0]][pop_value[0][1]] == "L":
    print("laber 발견!!")
    find_laber = 1
    laber_count = pop_value[1]
    break

  for i in range(4):
    new_x = pop_value[0][0] + dx[i]
    new_y = pop_value[0][1] + dy[i]

    if new_x >=0 and new_x <len(maps) and new_y >= 0 and new_y <len(maps[0]) and visit[new_x][new_y] == 0 :
      if maps[new_x][new_y] != "X":
        visit[new_x][new_y] = 1
        my_q.append([[new_x,new_y], pop_value[1] + 1 ])

if find_laber == 1:
  #label부터 
  print("-----------------------end 찾기 -------------------------")
  visit = [[ 0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
  my_q = deque([[laber, laber_count]]) # 좌표 / 
  while True:# end 찾기
    print("===========================")
    if len(my_q)== 0 :
      break
    pop_value = my_q.popleft()
    print(pop_value)
    
    if maps[pop_value[0][0]][pop_value[0][1]] == "E":
      print("laber 발견!!")
      E_find = 1
      laber_count = pop_value[1]
      break

    for i in range(4):
      new_x = pop_value[0][0] + dx[i]
      new_y = pop_value[0][1] + dy[i]

      if new_x >=0 and new_x <len(maps) and new_y >= 0 and new_y <len(maps[0]) and visit[new_x][new_y] == 0 :
        if maps[new_x][new_y] != "X":
          visit[new_x][new_y] = 1
          my_q.append([[new_x,new_y], pop_value[1] + 1 ])

if E_find == 1:
  answer = laber_count
else:
  answer = -1
  
print(answer)
