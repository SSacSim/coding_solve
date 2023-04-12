import sys
input = sys.stdin.readline
V, E = map(int,input().strip().split(" "))
inf = 99999999
matrix = [[ 0 if i == j else inf for i in range(V + 1 )] for j in range( V + 1 )]
for _ in range(E):
  start_, end_, weight_ = map(int,input().strip().split(" "))
  matrix[start_][end_] = weight_
# 플로이드 워셜 알고리즘

#for via for start for end
for via_ in range(1,V+1):
  for start_ in range(1,V+1):
    for end_ in range(1,V+1):
      if matrix[start_][end_] > matrix[start_][via_] + matrix[via_][end_]:
        matrix[start_][end_] = matrix[start_][via_] + matrix[via_][end_]
        
total_min = inf *10
for start_ in range(1 , V+ 1 ):
  for via_ in range(1, V + 1):
    if start_ == via_:
      continue
    if total_min > matrix[start_][via_] + matrix[via_][start_]:
      total_min = matrix[start_][via_] + matrix[via_][start_]

if total_min >= inf:
  print(-1)
else:
  print(total_min)
