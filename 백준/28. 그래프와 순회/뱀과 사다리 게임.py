#목표 100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.
N,M = map(int,input().split(" ")) # N : 사다리 수 , M = 뱀의 수 

log = [0 for i in range(101)]
for _ in range(N + M): # 사다리 이동 위치 표시
  x ,y = map(int,input().split(" "))
  log[x] = y
    
visit = [0 for i in range(101)]
visit[1] = 1
from collections import deque
my_q = deque([[1,0]]) # index ,count

find = 0
answer = 0
while True:
  if len(my_q) == 0 or find == 1:
    break

  pop_list = my_q.popleft()
  now_location = pop_list[0]
  now_count = pop_list[1]
  for i in range(1,7): # 주사위
    if now_location + i <= 100 and visit[now_location + i] == 0:
      visit[now_location + i] = 1
      if log[now_location + i ] == 0:
        next_location = now_location + i 
      else:
        next_location =  log[now_location+i]
      if next_location == 100:
        answer = now_count + 1
        find = 1
        break
      my_q.append([next_location, now_count + 1])
print(answer)
