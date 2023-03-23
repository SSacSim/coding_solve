from collections import deque
import sys
input = sys.stdin.readline

M,N = map(int,input().split(" "))
matrix = []
visit = [[0 for _ in range(M )] for _ in range(N )]
for i in range(N):
  matrix.append(list(map(int,input().split(" "))))

my_q = deque([])
visit = [[0 for _ in range(M )] for _ in range(N )]
count = 0
for i in range(N): #행 
  for j in range(M): # 열
    if matrix[i][j] == 1:
      my_q.append([j,i,0]) #x,y형태
      count += 1
      visit[i][j] = 1
    elif matrix[i][j] == -1:
      count += 1
    
# 가로x = M , 세로 y = N
dx = [1,0,-1,0] # 좌 하 우 상  
dy = [0,1,0,-1]
answer = 0
while True:
  if len(my_q) == 0:
    break
  
  pop_list = my_q.popleft() # 하나 추출 # x,y
  now_x = pop_list[0]
  now_y = pop_list[1]
  answer = pop_list[2]
  for i in range(4):
    new_x = now_x + dx[i]
    new_y = now_y + dy[i]
    if new_x < M and new_x >=0 and new_y < N and new_y >=0 and visit[new_y][new_x] == 0 and matrix[new_y][new_x]==0:
      visit[new_y][new_x] = 1
      my_q.append([new_x,new_y,pop_list[2]+1])
      count+=1
    
if count != M * N:
  print(-1)
else:
  print(answer)