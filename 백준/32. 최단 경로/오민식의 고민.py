########################## not solved
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

# 방문 가능한지 체크
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
  print('gg')

else:
  inf = -99999999999
  memo = [inf for _ in range(N)]
  memo[s] = node_visit[s]
  # 벨만 포드
  for index in range(N):
    for now_ in bus_matrix: # start , end, 사용 비용
      start_node = now_[0]
      end_node = now_[1]
      bus_money = now_[2]
      flag = 0
      # 현재 노드에서 최할 수 있는 최대값 - bus 이용료 + 다음 노드를 들렀을때 값
      if memo[start_node] + node_visit[end_node] - bus_money > memo[end_node]:
        memo[end_node] = memo[start_node] + node_visit[end_node] - bus_money
        if end_node == e:
          flag = 1
      # N 번 수행했을때 , 도착 노드에 업데이트가 있으면 도착 노드에 음의 폐로
    if index == N - 1:
      if flag:  
        print("Gee")
      else:
        if memo[e] <= inf:
          print("gg")
        else:
          print(memo[e])
