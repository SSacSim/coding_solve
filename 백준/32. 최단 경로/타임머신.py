import sys
input = sys.stdin.readline
# 벨만포드
N , V = map(int,input().split(" "))
load_ = []
for _ in range(V):
  s , e , w = map(int,input().split(" "))
  load_.append([s,e,w])
inf = 99999999
node_min = [inf for _ in range(N + 1)] # 1 base
node_min[1] = 0
# node의 V-1번 만큼 해야하는 이유
# 모든 노드를 살피고, len을 업데이트해야 하는데, length가 inf인경우가 먼저 나올 수 있으므로
# V-1번만큼 한다면, 모든 노드에서의 최소값을 보장함.
for i in range(V): 
  change_flag = 0  # 0 > 바뀌지 않았다
  for j in load_:
    start_node = j[0]
    end_node = j[1]
    weigth_ = j[2]

    # 시작 지점이 업데이트가 된 경우
    if node_min[start_node] != inf : 
      #end node까지 len update
      if node_min[end_node] > node_min[start_node] + weigth_:
        node_min[end_node] = node_min[start_node] + weigth_
        change_flag= 1
  
  # 만약, 변경된 length가 존재하지 않는 경우
  if change_flag == 0:    
    break
if change_flag == 1:
  print(-1)
else:
  for i in range(2,N + 1):
    if node_min[i] >= inf:
      print("-1")
    else:
      print(node_min[i])  
