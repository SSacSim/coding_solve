n =3 
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
visit = [[0 for _ in range(n)] for _ in range(n)]
# bfs 
from collections import deque
my_que = deque()
count = 0
for k in range(n):
  if visit[k][k] == 0:
    my_que.append(k)
    count +=1
    
  while True:
    if len(my_que) == 0:
      print("break")
      break

    target = my_que.popleft()

    for j in range(n):
      if computers[target][j] == 1 :
        if (visit[target][j] == 0) and (visit[j][target] == 0):
          visit[target][j] =1
          visit[j][target] =1
          my_que.append(j)

    print("my_que:",my_que)
print(count)
