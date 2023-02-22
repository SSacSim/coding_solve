places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from collections import deque
import copy
total_answer = []
for i in places:
  print("==================")
  matrix = []
  visit = []
  count = 0
  dx = [0,1,0,-1]
  dy = [1,0,-1,0]

  for j in i:
    answer = 0
    matrix.append(list(j))
    visit.append([0 for _ in range(len(list(j)))])

  count = 0
  answer = 1
  dx = [0,1,0,-1]
  dy = [1,0,-1,0]
  print(visit)


  # bfs를 통하여 하나라도 2칸씩 갔을때 사람을 만나면 XXXXX
  my_q = deque([]) # 현재위치, 지금까지 거리

  # 사람이 있는곳 que에 넣기
  for x in range(5):
    for y in range(5):
      if matrix[x][y] == "P" : 
        temp_visit =copy.deepcopy(visit)
        temp_visit[x][y] = 1
        my_q.append([x,y,0,temp_visit])

  meet_P = 0
  # 사람 있는 곳 기준으로 범위 2안에 다른 사람이 있는지 확인
  while True:
    print("my_q",my_q)
    if len(my_q) == 0 or meet_P == 1:
      total_answer.append(answer)
      break
    
    pop_value = my_q.popleft()
    # 4방향 확인 (우 하 좌 상)
    for i in range(4):
      if pop_value[2] >= 2:
        count =+1
        break
      if pop_value[0] + dx[i] >=0 and pop_value[0] + dx[i] <=4 and pop_value[1] + dy[i] >=0 and pop_value[1] + dy[i] <=4: # 범위 안에 들면
        if matrix[pop_value[0] + dx[i]][pop_value[1] + dy[i]] == "O" and pop_value[2] <= 2 and pop_value[3][pop_value[0] + dx[i]][pop_value[1] + dy[i]] == 0:
          pop_value[3][pop_value[0] + dx[i]][pop_value[1] + dy[i]] = 1
          temp_visit =pop_value[3] 
          my_q.append([pop_value[0]+ dx[i],pop_value[1]+ dy[i],pop_value[2]+1 , temp_visit ])
        elif  matrix[pop_value[0] + dx[i]][pop_value[1] + dy[i]] == "P" and pop_value[2] <= 2 and pop_value[3][pop_value[0] + dx[i]][pop_value[1] + dy[i]] == 0:
          print("만낫다!!!!!")
          print(pop_value)
          print(pop_value[0] + dx[i] , pop_value[1] + dy[i])
          print(visit)
          meet_P = 1
          answer = 0
          break
  
print(total_answer)