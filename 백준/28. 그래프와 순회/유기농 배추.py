from collections import deque
import sys
input = sys.stdin.readline
T = int(input().strip())
dx = [1,0 , -1 ,0]
dy = [0,1 ,0, -1]

for _ in range(T):
  M,N,K = map(int,input().strip().split(" ")) # M = X, N = Y
  matrix =[ [0 for _ in range(M)] for _ in range(N)]
  # 배추 입력부
  for _ in range(K):
    x , y = map(int,input().strip().split(" "))
    matrix[y][x] = 1

  #
  my_q = deque([])
  count = 0
  visit = [ [0 for _ in range(M)] for _ in range(N)]

  #matrix[y][x] 형태임
  for i in range(N): # Y
    for j in range(M) : # X
      if matrix[i][j] == 1 and visit[i][j] == 0: # 배추가 심어져 있는 곳인데, 방문하지 않은곳

        visit[i][j] = 1 # 방문 표시
        my_q.append([j,i]) # x, y형태
        count += 1

        while True: #bfs
          if len(my_q) == 0:
              break
          pop_x,pop_y = my_q.popleft()
          
          for k in range(4): # 상하좌우 
            new_x = pop_x + dx[k]
            new_y = pop_y + dy[k]
            
            # 조건에 맞으면 q에 넣음
            if new_x >=0 and new_x<M and new_y >=0 and new_y <N and \
              matrix[new_y][new_x] == 1 and visit[new_y][new_x] == 0:
              my_q.append([new_x,new_y])
              visit[new_y][new_x] = 1
  print(count)
