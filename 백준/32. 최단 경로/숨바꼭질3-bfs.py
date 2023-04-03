N, K = map(int,input().split(" "))
visit = [ 0 for _ in range(100001 *2 )]
from collections import deque

my_q = deque([])

my_q.append([N,0]) # 현재위치 이동시간
visit[N] = 1

while len(my_q) != 0:
  pop_list = my_q.popleft()
  if pop_list[0] == K:
    print(pop_list[1])
    break

  #순간이동 2*x / +0초
  temp3 = pop_list[0] *2 
  if temp3 > 0 and temp3 <= 100001 and visit[temp3] == 0:
    my_q.append([temp3 , pop_list[1]])
    visit[temp3] = 1
  if K == temp3:
    print(pop_list[1])
    break
    
  #걷기 x-1 , x + 1 / +1초
  temp1 = pop_list[0] - 1
  temp2 = pop_list[0] + 1
  if temp1 > 0 and visit[temp1] == 0:
    my_q.append([temp1 , pop_list[1] + 1])
    visit[temp1] =1 
  if temp2 <= 100001 and visit[temp2] == 0:
    my_q.append([temp2 , pop_list[1] + 1])
    visit[temp2] = 1

  if K in [temp1,temp2]:
    print(pop_list[1] + 1)
    break
