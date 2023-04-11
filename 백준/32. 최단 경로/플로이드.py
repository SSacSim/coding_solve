import sys
input = sys.stdin.readline
N = int(input())
V = int(input())

inf = 999999999
matrix = [[ 0 if i == j else inf for i in range(N +1 )] for j in range(N + 1)] # 1 base 
 
for _ in range(V):
  start_ , end_ , weight_ = map(int,input().split(" "))
  if matrix[start_][end_] >weight_:
    matrix[start_][end_] = weight_
    
# 플로이드 워셜 알고리즘 시작
for via_node in range(1, N + 1 ) : # 시작 지점
  for start_node in range(1, N + 1) : # 해당 노드를 거쳐서 만들수 있는 거리 ( 경유 node )
    for end_node in range(1,N + 1):
      if matrix[start_node][end_node] > matrix[start_node][via_node] + matrix[via_node][end_node] : 
        matrix[start_node][end_node] = matrix[start_node][via_node] + matrix[via_node][end_node]

for i in range(1,N+1):
  temp = []
  for j in range(1,N + 1 ):
    if matrix[i][j] >= inf:
      temp.append(0)
    else:
      temp.append(matrix[i][j])
  print(*temp)
