import sys
input = sys.stdin.readline

# 다익스트라 최소거리 알고리즘
V,E = map(int,input().split())
start_node = int(input())
inf = 9999999
matrix = dict()

for i in range(V + 1):
  matrix[i] = []
for _ in range(E):
  start_ , end_ , weight = list(map(int,input().split(" ")))
  matrix[start_].append([weight,end_])

import heapq
# 다익스트라로 최단거리 구하기
'''
  start_node : 시작 위치
  matrix : dict, key : {시작 지점 , [도착 노드, 가중치]}
  visit : node 방문 flag ,  list[ int ] , -1 : visit x / 1 : visit o
  
  수행 :
    1. 현재 node에서 갈 수 있는 node를 find. (func. find_to_node())
    2. 단, visit ( 최소 거리가 결정된 node 제외)이 -1인 곳만 탐색
    3. 기존 min_lenth할 수 있는 거리보다 작으면 min_lenth에 거리 update
    4. visit중 확정되지 않은 node의 길이가 가장 짧은 노드를 선택
    5. 1번 부터 반복
'''
visit = [-1 for _ in range(V + 1)] # 1-base
min_length = [inf for _ in range(V + 1)] # 1-base

now_node = start_node # now_node : 위치한 노드

min_q = [] # heap으로 사용할 자료구조
heapq.heappush(min_q, [0 , now_node]) #[ 거리, 현재 노드 ]

while len(min_q) != 0: # 모든 노드를 확정지을때까지
  # heappop를 하여 next node를 판별
  pop_list = heapq.heappop(min_q)
  
  # 만약, 현재 pop된 node까지의 거리가 기록된(min_length)보다 크면, 진행 x
  if min_length[pop_list[1]] < pop_list[0]:
    continue

  #pop 된 순간 방문한것 
  visit[pop_list[1]] = 1 # 시작 node visit 방문 체크
  min_length[pop_list[1]] = pop_list[0]

  # pop_list[1]은 현재 노드 
  # zip( dist, next_node )
  for i in matrix[pop_list[1]]: # [dist, next_node]
    if visit[i[1]] != 0:
      next_node = i[1]
      next_node_length =  pop_list[0]+ i[0]
    
    # dist list update
      if min_length[next_node] > next_node_length:
        min_length[next_node] = next_node_length

        # heapq에 넣기
        heapq.heappush(min_q, [next_node_length , next_node])

for i in min_length[1:]:
  if i == inf:
    print("INF")
  else:
    print(i)
