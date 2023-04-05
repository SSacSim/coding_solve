import heapq
import sys
input = sys.stdin.readline
# N < 800, E < 200,000
N, E = map(int,input().split(" "))

# 인접행렬로 구성
matrix = dict()

for i in range(N + 1):
  matrix[i] = []

# 양방향 데이터임
for _ in range(E):
  start_ , end_ ,weight_ = map(int,input().split(" "))

  matrix[start_].append([weight_,end_])
  matrix[end_].append([weight_,start_])

v1 , v2 = map(int,input().split(" "))
visit = [ 0 for _ in range(N + 1)]

# start - 1 다익스트라
inf = 9999999999999

# 다익스라 함수 
def find_min_length(start_node):
  hq = []
  visit = [ 0 for _ in range(N + 1)]
  min_length = [ inf for _ in range(N + 1)]
  min_length[start_node] = 0

  heapq.heappush(hq, [0 , start_node]) # [len, start_node]

  while len(hq) != 0:
    # pop되는 것은 최소값임, 이때 visit 표시
    # pop_[0] = 최소길이, pop_[1] = now_node
    pop_ = heapq.heappop(hq)
    now_node = pop_[1]

    # 방문 표시
    visit[now_node] = 1

    # 다음 노드 후보 선택 후 hq input
    # 조건 1. visit = 0 일것,
    # 조건 2. min_lenght보다 작을 것.
    for i in matrix[now_node]: # [weight, node]
      next_node = i[1]

      if visit[next_node] == 0: # 방문하지 않은 곳이라면 
        if min_length[now_node] + i[0] < min_length[next_node]: # 시작점 + 도착점 < 기존 도착점
          min_length[next_node] = min_length[now_node] + i[0] # 도착점 min_len  update
          heapq.heappush(hq, [ min_length[next_node] ,next_node]) 

  return min_length
task1 = find_min_length(1) # 시작점부터 모든 최소거리 구함
task2 = find_min_length(v1) # v1에서 N까지 최소거리  
task3 = find_min_length(v2) # v2에서 N까지 최소거리

answer = min(task1[v1] + task2[v2] + task3[N] , task1[v2] + task3[v1] + task2[N])
if answer >= inf:
  print(-1)
else:
  print(answer)
