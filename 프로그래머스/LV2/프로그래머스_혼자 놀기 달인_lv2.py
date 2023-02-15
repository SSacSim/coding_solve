cards = [8,6,3,7,2,5,1,4]

# bfs
from collections import deque

my_q = deque([[cards[0],1]])

visit = [0 for _ in range(max(cards) + 1 )] # 1base
visit[1] = 1

answer = 0
box = []
while True:
  print("--------------------------")
  print("my_q", my_q)
  print("visit",visit)
  if len(my_q) == 0:
    break
  pop_number = my_q.popleft()
  print("pop_number",pop_number)
  if visit[pop_number[0]] == 0:
    visit[pop_number[0]] = 1
    my_q.append([cards[pop_number[0]-1] , pop_number[1] + 1])# 박스안 숫자, 현재 같은 박스에 들어간 수
  else:
    box.append(pop_number[1])
    print("else 실행")
    for j in range(len(cards)):
      if visit[j+1] == 0 :
        my_q.append([cards[j], 1])
        visit[j+1] = 1
        break
box.sort()
if len(box) != 1:
   answer = box[-1] * box[-2]

print(answer)
