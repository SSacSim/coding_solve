n = 5
roads = 	[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = 	[1, 3, 5]
destination = 5

visit = [0 for _ in range(n + 1)]
visit_len = [-1 for _ in range(n + 1)]

edge = dict()

for i in roads:
  if i[0] not in edge:
    edge[i[0]] = [i[1]]
  else:
    edge[i[0]].append(i[1])

  if i[1] not in edge:
    edge[i[1]] = [i[0]]
  else:
    edge[i[1]].append(i[0])

# bfs
from collections import deque
answer = []

my_que = deque([])
my_que.append([destination,0]) # node
visit[destination] = 1
visit_len[destination] = 0

while True:
  if len(my_que) == 0:
    break
  print("my_que",my_que)
  now_node, count = my_que.popleft()

  print("now_node",now_node)
  print("count",count)
  for j in edge[now_node]:
    print("j",j)
    if visit[j] == 0: # 방문하지 않은 곳이라면
      visit[j] = 1
      visit_len[j] = count+1
      
      my_que.append([j,count+1])

print("====================")

answer= []
for i in sources:
  answer.append(visit_len[i])

print(answer)