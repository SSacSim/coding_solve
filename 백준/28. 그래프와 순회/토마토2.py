from collections import deque
import sys
input = sys.stdin.readline
M,N ,H = map(int,input().strip().split())
# 정수 1은 익은 토마토
# 정수 0 은 익지 않은 토마토
# 정수 -1은 토마토가 들어있지 않은 칸
# M = x, N = y, h = z
tomato_matrix = []

for _ in range(H):
  height_ = []
  for _ in range(N):
    height_.append(list(map(int,input().strip().split(" "))))
  tomato_matrix.append(height_)

total_tomato = 0
my_q = deque([])
visit = [ [ [0 for _ in range(len(tomato_matrix[0][0]))] for _ in range(len(tomato_matrix[0]))] for _ in range(len(tomato_matrix))]
# tomato_matrix[H][N][M] # z,y,x순 
# 이미 1인 곳 deque에 넣기
for z in range(H): #depth
  for y in range(N): # 높이
    for x in range(M): # 가로
      if tomato_matrix[z][y][x] != 0:
        total_tomato += 1
      if tomato_matrix[z][y][x] == 1:
        my_q.append([z,y,x , 0])
        visit[z][y][x] = 1

#시계방향 (우 하 좌 상 ) / depth ( )
dx =[1, 0, -1,0, 0, 0]
dy= [0,-1, 0, 1, 0, 0]
dz =[0 ,0, 0, 0, 1, -1]
answer = 0
while True:
  if len(my_q) == 0:
    break
  # popleft 수행
  # pop_구성 = [z,y,x, 지나온 거리]
  pop_ = my_q.popleft()

  # x,y,z,가 각각 범위에 들어왔는가? and 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 matrix 값이 0인가? and visit은 0인가?
  for i in range(6):
    new_z = pop_[0] + dz[i]
    new_y = pop_[1] + dy[i]
    new_x = pop_[2] + dx[i]

    if (new_z >= 0 and new_z < H) and (new_y >= 0 and new_y < N) and (new_x >= 0 and new_x < M): # x,y,z 범위 체킹
      if tomato_matrix[new_z][new_y][new_x] == 0:# 토마토가 없는 곳인지 체킹
        if visit[new_z][new_y][new_x] == 0: # 방문한 곳인지 아닌지 체킹
          # 모든 조건을 만족하였으므로 
          # 1. visit 체킹
          visit[new_z][new_y][new_x] = 1
          # 2. que에 넣기
          my_q.append([new_z,new_y,new_x,pop_[3] + 1])
          # 3. 토마토 총 갯수를 알기위한 count 증가
          total_tomato += 1
          if answer < pop_[3] + 1:
            answer = pop_[3] + 1
if total_tomato != M * N * H:
  print(-1)
else:
  print(answer)from collections import deque
import sys
input = sys.stdin.readline
M,N ,H = map(int,input().strip().split())
# 정수 1은 익은 토마토
# 정수 0 은 익지 않은 토마토
# 정수 -1은 토마토가 들어있지 않은 칸
# M = x, N = y, h = z
tomato_matrix = []

for _ in range(H):
  height_ = []
  for _ in range(N):
    height_.append(list(map(int,input().strip().split(" "))))
  tomato_matrix.append(height_)

total_tomato = 0
my_q = deque([])
visit = [ [ [0 for _ in range(len(tomato_matrix[0][0]))] for _ in range(len(tomato_matrix[0]))] for _ in range(len(tomato_matrix))]
# tomato_matrix[H][N][M] # z,y,x순 
# 이미 1인 곳 deque에 넣기
for z in range(H): #depth
  for y in range(N): # 높이
    for x in range(M): # 가로
      if tomato_matrix[z][y][x] != 0:
        total_tomato += 1
      if tomato_matrix[z][y][x] == 1:
        my_q.append([z,y,x , 0])
        visit[z][y][x] = 1

#시계방향 (우 하 좌 상 ) / depth ( )
dx =[1, 0, -1,0, 0, 0]
dy= [0,-1, 0, 1, 0, 0]
dz =[0 ,0, 0, 0, 1, -1]
answer = 0
while True:
  if len(my_q) == 0:
    break
  # popleft 수행
  # pop_구성 = [z,y,x, 지나온 거리]
  pop_ = my_q.popleft()

  # x,y,z,가 각각 범위에 들어왔는가? and 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 matrix 값이 0인가? and visit은 0인가?
  for i in range(6):
    new_z = pop_[0] + dz[i]
    new_y = pop_[1] + dy[i]
    new_x = pop_[2] + dx[i]

    if (new_z >= 0 and new_z < H) and (new_y >= 0 and new_y < N) and (new_x >= 0 and new_x < M): # x,y,z 범위 체킹
      if tomato_matrix[new_z][new_y][new_x] == 0:# 토마토가 없는 곳인지 체킹
        if visit[new_z][new_y][new_x] == 0: # 방문한 곳인지 아닌지 체킹
          # 모든 조건을 만족하였으므로 
          # 1. visit 체킹
          visit[new_z][new_y][new_x] = 1
          # 2. que에 넣기
          my_q.append([new_z,new_y,new_x,pop_[3] + 1])
          # 3. 토마토 총 갯수를 알기위한 count 증가
          total_tomato += 1
          if answer < pop_[3] + 1:
            answer = pop_[3] + 1
if total_tomato != M * N * H:
  print(-1)
else:
  print(answer)
