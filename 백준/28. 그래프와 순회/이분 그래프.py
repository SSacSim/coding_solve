from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
  V, E = map(int,input().split(" "))
  matrix_dict = { x : [] for x in range(1,V+1)}

  for _ in range(E):
    start_ , end_ = map(int,input().split(" "))
    matrix_dict[start_].append(end_)
    matrix_dict[end_].append(start_)

  visit = [0 for _ in range(V+1)] # 1base
  color = [None for _ in range(V+1)]
  #bfs
  
  for i in range(1, V+1):
    if visit[i] == 0:
      my_q = deque([[i , True]])
      visit[i] = 1

      color[i] = True
      now_color = False

      same_color_flag = 0
      while True:

        if len(my_q) == 0 or same_color_flag:
          break

        start_node , now_node_color = my_q.popleft()
        for next_node in matrix_dict[start_node]:
          if visit[next_node] == 0 :
            my_q.append([next_node , not now_node_color])
            color[next_node] = not now_node_color
            visit[next_node] = 1
          else:
            if color[start_node] == color[next_node]:
              same_color_flag = 1
              break
      if same_color_flag:
        break

  if same_color_flag:
    print("NO")
  else:
    print("YES")
