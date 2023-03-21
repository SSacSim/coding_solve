import sys
input = sys.stdin.readline
N, M , V = map(int,input().strip().split(" "))
matrix = [[ 0 for _ in range(N + 1)] for _ in range(N + 1)] # 1 base
visit = [ 0 for _ in range(N + 1)] # base
for _ in range(M):
  in_ , out_ = map(int,input().strip().split(" "))
  matrix[in_][out_] = 1
  matrix[out_][in_] = 1
dfs_visit = [ 0 for _ in range(N + 1)] # base
dfs_visit[V] = 1
answer = [V]

# dfs
# 재귀로 구현 시도
# 시작지점, 가장 빠르게 만나는 지점

def dfs(start_node,answer =[]):
  #find next node
  for i in range(1,N+1):
    if matrix[start_node][i] == 1 and dfs_visit[i] == 0:
      dfs_visit[i] = 1
      answer.append(i)
      dfs(i,answer)
  return answer

answer += dfs(V)
print(*answer)

answer = []
visit[V] = 1
#bfs

from collections import deque

my_q = deque([])

my_q.append(V) # 시작점
answer = [V]
while True:
  if len(my_q) == 0:
    print(*answer)
    break
  
  next_node = my_q.popleft()

  for i in range(1,N + 1):
    if matrix[next_node][i] == 1 and visit[i] == 0: # 연결되어 있고, 방문하지 않았으면 추가
      visit[i]= 1
      answer.append(i)
      my_q.append(i)
