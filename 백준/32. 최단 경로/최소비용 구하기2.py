import heapq
import sys
input = sys.stdin.readline

# 최소비용 구하기 2
n = int(input().strip())
m = int(input().strip())

matrix = {}
for _ in range(m):
  temp = list(map(int,input().strip().split(" ")))
  
  if temp[0] not in matrix:
    matrix[temp[0]] = [[temp[1] , temp[2]]] # key : 시작 노드 , value : [ 도작 노드1 , 거리 ]
  else:
    matrix[temp[0]].append([temp[1],temp[2]])

s, e = map(int,input().strip().split(" "))

inf = 9999999999
memo = [ inf for _ in range(n+1)] # 1base
visit = [ 0 for _ in range(n+1)] # 1base
node_memo = [ inf for _ in range(n+1)]
memo[s] = 0 # 시작점 거리 체크

heap_list = []

heapq.heappush(heap_list, [0 , [s]]) # 거리 , 지나간 노드

while heap_list:
  if visit[e] != 0:
    break
  pop_ = heapq.heappop(heap_list) # 거리, 지나간 노드
  now_len = pop_[0]
  now_node = pop_[1][-1] # list 이므로 맨 마지막이 가장 최근의 노드

  visit[now_node] = 1
  # 현재 노드에서 갈 수 있는 모든 노드 탐색
  if now_node in matrix : 
      for next_ in matrix[now_node]: # next_ : [0] = 연결된 노드 , [1] = 거리
        if visit[next_[0]] == 0 :
          # memo update
          # 현재 노드까지 거리 + next node 까지 거리 < 기존 next_node 까지의 거리 
          if memo[now_node] + next_[1] < memo[next_[0]]:
            memo[next_[0]] = memo[now_node] + next_[1]
            node_memo[next_[0]] = pop_[1] + [next_[0]]
            heapq.heappush(heap_list, [memo[next_[0]] , pop_[1] + [next_[0]]])

print(memo[e])
print(len(node_memo[e]))
print(*node_memo[e])
