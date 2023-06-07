import sys
from collections import deque
input = sys.stdin.readline

N ,s ,e , m = list(map(int,input().strip().split(" ")))
bus_matrix = []
bus_dict = {}
for _ in range(m):
  temp_in = list(map(int,input().strip().split(" ")))
  bus_matrix.append(temp_in)


  if temp_in[0] not in bus_dict:
    bus_dict[temp_in[0]] = [ [temp_in[1] , temp_in[2]] ]
  else:
    bus_dict[temp_in[0]].append([temp_in[1] , temp_in[2]]) 
node_visit = list(map(int,input().strip().split(" ")))

def bfs(s , e ):
    # 방문 가능한지 check : bfs
    my_q = deque([s]) # start
    visit = [ 0 for _ in range(N)] 
    while my_q:
        now_node = my_q.popleft()
        visit[now_node] = 1
        if now_node in bus_dict:
            for next_node_ in bus_dict[now_node]:
                if visit[next_node_[0]] == 0:
                    my_q.append(next_node_[0])

    if visit[e] == 0 :
        return 0 , visit# 갈 수 없음
    else:
        return 1 , visit# 갈 수 있음
    # 사이클이 있는데... 그 사이클이 end에 영향을 주냐? 
return_num , visit = bfs(s,e)
if return_num == 0:
    print("gg")
else:
  inf = -999999999
  memo = [inf for _ in range(N)]
  memo[s] = node_visit[s]
  # 벨만 포드
  cycle = []
  for index in range(N):
    flag = 0
    for now_ in bus_matrix: # start , end, 사용 비용
      start_node = now_[0]
      end_node = now_[1]
      bus_money = now_[2]
      # 현재 노드에서 최할 수 있는 최대값 - bus 이용료 + 다음 노드를 들렀을때 값
      if memo[start_node] + node_visit[end_node] - bus_money > memo[end_node]:
        memo[end_node] = memo[start_node] + node_visit[end_node] - bus_money
        flag = 1
        if index == N-1:
          if start_node not in cycle:
            cycle.append(start_node)
      # N 번 수행했을때 , 도착 노드에 업데이트가 있으면 도착 노드에 음의 폐로
    temp = 0
    if index == N - 1:
      for k in cycle:
        return_num_e , temp_visit_e = bfs(k , e)
        return_num_s , temp_visit_s = bfs(s , k)
        if return_num_s == 1 and return_num_e == 1:
          temp = 1 # cycle에서 start를 거쳐 end로 갈 수 있을때
          break
      if temp == 0: # cycle에서 end로 갈 수 없는 경우
        if visit[e] == 1: # 시작점에서 end로 갈 수 있는 경우
          print(memo[e])
      else:
        print("Gee")