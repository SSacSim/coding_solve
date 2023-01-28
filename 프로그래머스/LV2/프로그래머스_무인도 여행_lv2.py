maps = ["X591X","X1X5X","X231X", "1XXX1"]
row = len(maps)
column = len(maps[0])

visit = [[ 0 for _ in range(column)] for _ in range(row)]
new_map = [ list(i) for i in maps]

from collections import deque

now_row = 0
now_column = 0  
my_que = deque([])
# 상우하좌
x=[0,1,0,-1] # 좌우
y=[-1,0,1,0] # 상하
answer = []
for i in range(row):
  for j in range(column):
    now_row = i
    now_column = j  
    
    if new_map[now_row][now_column] == "X" or visit[now_row][now_column] ==1:
      continue
    my_que.append([now_row,now_column])
    
    print("i,j",i,j)
    print("my_que",my_que)
    print("visit",visit)
    value = int(new_map[now_row][now_column])
    visit[now_row][now_column] =1


    while True:
      if len(my_que) == 0:
        if value !=0:
          answer.append(value)
        break
      print("while 안 que",my_que)
      pop_row ,pop_column = my_que.popleft()

      # 상하좌우
      for k in range(4):
        next_row = pop_row +y[k]
        next_column = pop_column + x[k]
        if (next_row >=0 and next_row < row) and (next_column >=0 and next_column < column): #범위에 들었을때
          if visit[next_row][next_column] == 0: #방문하지 않은곳
            if new_map[next_row][next_column] != "X":
              my_que.append([next_row,next_column])
              value += int(new_map[next_row][next_column])
            visit[next_row][next_column] = 1
  print("==========================")

if len(answer) == 0:
  answer.append(-1)

answer.sort()
print(answer)
