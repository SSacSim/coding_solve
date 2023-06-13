import sys
input = sys.stdin.readline
N , L , R = map(int,input().strip().split(" "))
matrix = []

for _ in range(N):
  matrix.append(list(map(int,input().strip().split(" "))))

import copy
from collections import deque
# 우 하 좌 상
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0 ,-1]

my_q= deque([]) # s_row, s_column

# 모든 지점을 한번씩 보았나 체크하는 visit
answer = 0

while True:
  group = 0  
  transform_visit = [[ 0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  
  change_flag = 0
  for row in range(len(matrix)): # row
    for column in range(len(matrix[0])): # column
      total_sum = 0
      total_maeul = [[row,column]]
      # 이미 한번 방문했다면 pass
      if transform_visit[row][column] == 1:
        continue
      my_q.append([row,column]) # 임시 test
      # 이번 bfs에서 바뀐 부분만 알기위한 visit
      
      # 이전 세팅
      transform_visit[row][column] = 1

      while my_q:
        now_row, now_column = my_q.popleft()
        total_sum += matrix[now_row][now_column]

        for i in range(4):
          next_row = now_row + dy[i]
          next_column = now_column + dx[i]

          # boundary check
          if next_row >= 0 and next_row < len(matrix) and next_column >= 0 and next_column < len(matrix[0]):
            calcu = abs(matrix[next_row][next_column] - matrix[now_row][now_column]) # 각 마을별 인원수 차이
            
            if calcu >= L and calcu <= R and transform_visit[next_row][next_column] == 0 :
              transform_visit[next_row][next_column] = 1
              total_maeul.append([next_row,next_column])
              my_q.append([next_row,next_column])

      if len(total_maeul) >=2 : # 다른 곳을 방문할때
        change_flag = 1
        # 한번 종료시 
      for i in total_maeul:
        matrix[i[0]][i[1]] = total_sum // len(total_maeul)
  # 모든 순회를 마치고 한번이라도 바뀐경우         
  if change_flag == 1:
    answer += 1
  else:
    break
print(answer)
