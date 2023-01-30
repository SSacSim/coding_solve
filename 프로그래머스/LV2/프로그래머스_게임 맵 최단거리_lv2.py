maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

#bfs 
from collections import deque
my_que = deque([])
visit = [[ 0 for i in range(len(maps[0]))]  for j in range(len(maps)) ] # 1base

ylen = len(maps)
xlen = len(maps[0])

my_que.append([0,0,0])
visit[0][0] = 1
while True:
  print("my_que",my_que)

  if len(my_que) == 0:
    answer= -2
    break
  
  pop_location = my_que.popleft()

  if pop_location[0] == ylen- 1and pop_location[1] == xlen-1:
    answer = pop_location[2]
    break

  for i in range(4):
    next_y = pop_location[0] + dy[i]
    next_x = pop_location[1] + dx[i]

    if next_y >=0 and next_y <ylen and next_x >=0 and next_x <xlen :
      if maps[next_y][next_x] == 1 and visit[next_y][next_x] == 0:
        visit[next_y][next_x] = 1
        my_que.append([next_y, next_x,pop_location[2] + 1 ])
print(answer)